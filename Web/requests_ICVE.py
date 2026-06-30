import time
import requests


# 获取账号信息
def get_userinfo(_token):
    """获取账号信息"""
    url = f"https://sso.icve.com.cn/prod-api/user/userInfo?token={_token}"
    res = requests.post(url)
    re_js = res.json()
    return re_js['data']



# 获取登录凭证/Bearer 令牌串
def get_authorization(_token):

    """# 获取登录凭证/Bearer 令牌串"""
    url = "https://zjy2.icve.com.cn/prod-api/auth/passLogin?token="+_token

    res = requests.get(url)
    rs_json = res.json()
    if rs_json['data']['notAllowLoginMsg'] == '':
        authorization = rs_json['data']['access_token']
        return authorization
    return ''



def get_classroom_list(_authorization, size):
    """
    获取课堂列表
    ->
    """
    url = f"https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachInfo/student/list?pageNum=1&pageSize={size}&isCriteria=1"
    headers = {
        "Authorization": _authorization
    }
    res = requests.get(url, headers=headers)
    rj = res.json()

    return rj['rows']


def get_course_detail_list(_authorization, _id) -> str:
    """
    获取课堂活动详情/id（签到ID
    _authorization: 登录令牌
    _id : 课堂活动唯一ID
    """
    url = f"https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachInfo/v2/student/info?id={_id}&requireType=2"
    headers = {
        "Authorization": _authorization
    }
    res = requests.get(url, headers=headers)
    rj = res.json()
    print(rj['data'])
    return rj['data']

# 签到接口
def scan_to_check_in(_authorization, classroom_id):
    # 获取当前13位毫秒时间戳
    now_13ts = int(time.time() * 1000)
    print("当前13位时间戳:", now_13ts)

    url = f"https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachSign/verifyQrCode?id={classroom_id}&qrCodeNumber={now_13ts}"
    headers = {
        "Authorization": _authorization
    }

    res = requests.get(url, headers=headers)
    return res.json()