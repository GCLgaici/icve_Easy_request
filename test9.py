import requests

url = "https://zjy2.icve.com.cn/prod-api/spoc/courseFaceTeachInfo/v2/student/info?id=657BB3EF-BC10-4DA5-AB56-A40816EC41DA&classId=A7F0FD31-686B-4151-B3C2-3838410147DE&courseId=6C48FFC4-9AD0-49AF-8249-C5E4ABB9F8B4&courseInfoId=7653FCB4-EBA5-4480-AAEA-4DFE61C3C9B6&requireType=2"
headers = {
  "Accept-Language": "h-CN,zh;q=0.8",
  "User-Agent": "ozilla/5.0 (Linux; U; Android 13; zh-cn; Mi 10 Build/TKQ1.221114.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1",
  "log-equipment-app-version": ".2.3",
  "log-equipment-model": "iaomi Mi 10",
  "log-equipment-api-version": "3",
  "log-equipment": "",
  "platform-type": "ndroid",
  "Authorization": "earer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiQkFFNDczMEItNkUyOS00RkE4LTgyMkUtNkE5ODk5MjUwNEQ0TjAiLCJ1c2VyX2tleSI6ImQwMDc3Y2JiLTA0MjAtNDhmNC1iOWIyLWQxOTA2NzE1Y2NkMiIsInVzZXJuYW1lIjoiZmpsenkyMDI1NTI0MDIzMiJ9.cj1RuYWAT-VkBsGrIxSvt5C9DuoS6nNg-tR4Mb24SoB0ADAbHmv62GkwxGfXWDiWHYH0AMqASXk2C6tC-UFEfw",
  "Host": "jy2.icve.com.cn",
  "Connection": "eep-Alive",
  "Accept-Encoding": "zip",
  "Cache-Control": "o-cache"
}

res = requests.get(url, headers=headers)
print(res.text)