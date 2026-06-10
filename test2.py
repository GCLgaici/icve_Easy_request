import requests
import json

url = "https://sso.icve.com.cn/api/v2/user/userLogin"
cookies = {
  "acw_tc": "781bad3d17810026772025946ea662ce69b54800e3cfc03b4342c301afd06f",
}

headers = {
  "Content-Type": "application/json;charset=UTF-8"
}
data0 = {
    "type":1,
    "userName":"fjlzy20255240234",
    "password":".Yy3593716",
    "captchaVerifyParam":"eyJjZXJ0aWZ5SWQiOiJyR0szTHkwWUpZIiwic2NlbmVJZCI6ImU3Z3l6MTAwIiwiaXNTaWduIjp0cnVlLCJzZWN1cml0eVRva2VuIjoiNm9PbzdlNzJuQTYxdVZMaVpWS2lMU2NGWlZiZDBSUERIcTQyc3REa2F3TU16bGlKeG0vWDRodGtmdWxKWmJHczd3SmZWVE90WFk4emZETzFzSys4L0lRSW5VR3cwYVRzejZjYndlS3JjNjBiaG5xaElwQzdTblJsSXhHUHNxdlgifQ==",
    "sceneId":"e7gyz100"
}
data = """{\"type\":1,\"userName\":\"fjlzy20255240234\",\"password\":\".Yy3593716\",\"captchaVerifyParam\":\"eyJjZXJ0aWZ5SWQiOiJyR0szTHkwWUpZIiwic2NlbmVJZCI6ImU3Z3l6MTAwIiwiaXNTaWduIjp0cnVlLCJzZWN1cml0eVRva2VuIjoiNm9PbzdlNzJuQTYxdVZMaVpWS2lMU2NGWlZiZDBSUERIcTQyc3REa2F3TU16bGlKeG0vWDRodGtmdWxKWmJHczd3SmZWVE90WFk4emZETzFzSys4L0lRSW5VR3cwYVRzejZjYndlS3JjNjBiaG5xaElwQzdTblJsSXhHUHNxdlgifQ==\",\"sceneId\":\"e7gyz100\"}"""
data2 = '{"type":1,"userName":"fjlzy20255240234","password":".Yy3593716","captchaVerifyParam":"eyJjZXJ0aWZ5SWQiOiJyR0szTHkwWUpZIiwic2NlbmVJZCI6ImU3Z3l6MTAwIiwiaXNTaWduIjp0cnVlLCJzZWN1cml0eVRva2VuIjoiNm9PbzdlNzJuQTYxdVZMaVpWS2lMU2NGWlZiZDBSUERIcTQyc3REa2F3TU16bGlKeG0vWDRodGtmdWxKWmJHczd3SmZWVE90WFk4emZETzFzSys4L0lRSW5VR3cwYVRzejZjYndlS3JjNjBiaG5xaElwQzdTblJsSXhHUHNxdlgifQ==","sceneId":"e7gyz100"}'



print(data)

res = requests.post(url, headers=headers, data=data2)
print(res.text)