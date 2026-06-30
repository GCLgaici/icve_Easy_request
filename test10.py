# 导入BeautifulSoup、TwoCaptcha、requests库
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha
import requests
# 2Captcha服务的API秘钥，你需要使用自己的
API_KEY = 'xxxxxxxxxxxxxx'
# 利用TwoCaptcha库，使用提供的API秘钥初始化一个solver对象，该对象可以解决ReCAPTCHA问题
solver = TwoCaptcha(API_KEY)
# 要抓取的网页的URL
url = "https://www.scrapebay.com/spam"
# 这是ReCAPTCHA的site key，可以从网页源码中找到。
site_key='6LfGNEoeAAAAALUsU1OWRJnNsF1xUvoai0tV090n'
# 这个函数用来获取CSRF token和cookies。它首先通过requests.get()获取页面内容，然后通过BeautifulSoup找到CSRF token。最后返回CSRF token和cookies。
def get_csrf_cookie(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    csrf_el = soup.select_one('[name=csrfmiddlewaretoken]')
    csrf = csrf_el['value']
    cokkies = response.cookies
    return csrf, cokkies
# 这个函数用来解决ReCAPTCHA问题。它使用TwoCaptcha solver对象的recaptcha()方法，如果发生异常则打印错误并退出。
def solve(url,sitekey):
    try:
        result = solver.recaptcha(sitekey=sitekey, url=url)
    except Exception as e:
        print(e)
        exit()
    return result
# 这个函数用来提交解决ReCAPTCHA后的页面。它首先构建一个POST请求的payload，然后通过requests.post()方法发送请求。最后返回网页的最后一列的文本。
def post_page(url, csrf, cookie, result):
    payload = 'csrfmiddlewaretoken={}&g-recaptcha-response={}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.scrapebay.com/spam'
    }
    response = requests.post(url,data=payload.format(csrf,result),headers=headers,cookies=cookie)
    soup = BeautifulSoup(response.text, "lxml")
    el = soup.select_one('td:last-child')
    return el.get_text()
# 先通过get_csrf_cookie(url)获取CSRF token和cookies，然后通过solve(url,site_key)解决ReCAPTCHA问题，最后通过post_page(url,csrf,cokkies,result)提交页面并打印出结果。
def main():
    csrf,cokkies = get_csrf_cookie(url)
    print("csrf:",csrf)
    print("cokkies:",cokkies)
    result = solve(url,site_key)
    print("captcha:",result)
    data = post_page(url,csrf,cokkies,result)
    print("result:",data)
if __name__ == "__main__":
    main()