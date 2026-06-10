import requests

url = "https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachSign/verifyQrCode?id=483BE9D8-C0DA-412C-AA5C-FCC502592178&qrCodeNumber=1781082564712&teachId=3EEC896B-FA00-408C-935F-EE577483B196"
headers = {
  "Accept-Language": "h-CN,zh;q=0.8",
  "User-Agent": "ozilla/5.0 (Linux; U; Android 13; zh-cn; Mi 10 Build/TKQ1.221114.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1",
  "log-equipment-app-version": ".2.2",
  "log-equipment-model": "iaomi Mi 10",
  "log-equipment-api-version": "3",
  "log-equipment": "",
  "platform-type": "ndroid",
  "Authorization": "earer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiQzUxOTU0NUUtODQ1NS00OTFCLUFGNkMtNEZGOEZDQkNGNEU0VVMiLCJ1c2VyX2tleSI6IjRiN2JjNDk5LThlMDQtNGY3ZC1iMGQ4LTkzOGVkOTQ0ZWMyMCIsInVzZXJuYW1lIjoiZmpsenkyMDI1NTI0MDIzNCJ9.FBvmrJ4KKRhdrlEQJOp6OVQfK45BGENeqVAldlRgOtPCzzQvAVXhx1Y7jFvZWCoN4LfSgy5gPR33mnpGVM4Srw",
  "Host": "jy2.icve.com.cn",
  "Connection": "eep-Alive",
  "Accept-Encoding": "zip",
  "Cache-Control": "o-cache"
}

res = requests.get(url, headers=headers)
print(res.text)