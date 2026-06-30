
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

