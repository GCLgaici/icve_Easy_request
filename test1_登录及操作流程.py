import time
import requests
import json

# 获取登录随机数
def login_random():
    url = "https://sso.icve.com.cn/api/v2/user/authenticate"

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "browserId": "1399ca7ca3111dd47896aac35743f3c"
        #"browserId": "c6aff242f391452187af0af189bf17c1"# 自己账号的browserId
    }
    data = {"userName": "fjlzy20255240234"}
    data = json.dumps(data)

    res = requests.post(url, headers=headers, data=data)
    re_js = res.json()
    print(re_js)
    return re_js['data']['random']



#用户登录
def login(num_sj):
    url = "https://sso.icve.com.cn/api/v2/user/userLogin"

    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    data = {
        "type":1,
        "userName":"fjlzy20255240234",
        "password":"Zjy2@fjlzy20255240233",
        "random":num_sj
    }
    data = json.dumps(data)

    res = requests.post(url, headers=headers, data=data)
    re_js = res.json()
    print(res.text)

    return re_js['data']['token']

# 获取登录凭证/Bearer 令牌串
def get_authorization(_token):
    url = "https://zjy2.icve.com.cn/prod-api/auth/passLogin?token="+_token

    res = requests.get(url)
    rs_json = res.json()
    print(res.json())
    authorization = rs_json['data']['access_token']
    print(authorization)
    return authorization




# 获取我加入的SPOC课程
def get_curriculum(_authorization, pageNum, pageSize):


    url = f"https://zjy2.icve.com.cn/prod-api/spoc/courseInfoStudent/app/myCourseList?pageNum={pageNum}&pageSize={pageSize}&isCriteria=1"
    headers = {
        # Bearer 令牌串
        "Authorization": _authorization
    }

    res = requests.get(url, headers=headers)
    print(res)
    res = res.json()
    print(res)


# 扫码
def scan_to_check_in0(_authorization, classroom_id, qrcode_number):

    url = f"https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachSign/generateData/{classroom_id}?qrCodeNumber={qrcode_number}"
    headers = {
        "Authorization": _authorization
    }

    res = requests.get(url, headers=headers)
    print(res.text)
    ...

# 签到接口
def scan_to_check_in(_authorization, classroom_id):
    # 获取当前13位毫秒时间戳
    now_13ts = int(time.time() * 1000)
    print("当前13位时间戳:", now_13ts)

    url = f"https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachSign/verifyQrCode?id={classroom_id}&qrCodeNumber={now_13ts}"
    headers = {
        "Authorization": _authorization
    }
    headers = {
        "Authorization": _authorization
    }
    print(url)
    res = requests.get(url, headers=headers)
    print(res.text)
    ...

if __name__ == '__main__':
    # dl_sj = login_random()
    # token = login(dl_sj)
    # authorization = get_authorization(token)
    authorization = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiQzUxOTU0NUUtODQ1NS00OTFCLUFGNkMtNEZGOEZDQkNGNEU0VVMiLCJ1c2VyX2tleSI6IjRiN2JjNDk5LThlMDQtNGY3ZC1iMGQ4LTkzOGVkOTQ0ZWMyMCIsInVzZXJuYW1lIjoiZmpsenkyMDI1NTI0MDIzNCJ9.FBvmrJ4KKRhdrlEQJOp6OVQfK45BGENeqVAldlRgOtPCzzQvAVXhx1Y7jFvZWCoN4LfSgy5gPR33mnpGVM4Srw"
    get_curriculum(authorization, 1, 14)
    scan_to_check_in(authorization, "483BE9D8-C0DA-412C-AA5C-FCC502592178")
    ...