import requests

url = "https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachSign/generateData/EEE22658-24FF-4472-87D9-F1A16CBD4526?qrCodeNumber=9780877198472"
headers = {
  "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiQzUxOTU0NUUtODQ1NS00OTFCLUFGNkMtNEZGOEZDQkNGNEU0VVMiLCJ1c2VyX2tleSI6ImFlZDU0ODNkLTk1YTAtNDhkMC04ZjAwLTQ3OTczNjcxMWU4ZCIsInVzZXJuYW1lIjoiZmpsenkyMDI1NTI0MDIzNCJ9.P5iMx3UF1BLggJti8jDvR1Ni9iJAqV2ZiN3ZOFQoubP3A143m3omNVZzcY2sHSuZpiykcetoErjVpiIx_x9dxw"
}

res = requests.get(url, headers=headers)
print(res.text)