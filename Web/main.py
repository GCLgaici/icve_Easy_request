import json
import time
from flask import Flask, request, jsonify, send_from_directory, render_template, redirect
from flask_sock import Sock
from Web.requests_ICVE import get_authorization,get_classroom_list,get_userinfo,get_course_detail_list, scan_to_check_in


# Todo 1. 客户端断开自动重连，连接失败自动重新注册
# Todo 2. 规范化服务器前后端以及客户端各种请求格式
# Todo 3. 修复有时在线客户机显示不在线的情况

# ================================ 初始化Flask应用 ================================
app = Flask(__name__)
sock = Sock(app)
HOST = '0.0.0.0'
PORT = 8080
gw_url = "https://icve.052024.xyz"
token_red_url = f"https://sso.icve.com.cn/sso/auth?mode=simple&source=2&redirect={gw_url}"
user_data_list = []

# ================================ 工具 ================================




# ================================ 基础路由 ================================
@app.route('/')
def index():
    return 'null'


@app.route('/login_push', methods=['GET', 'POST'])
def login_push():
    token = request.args.get('token')
    if not token:
        return redirect(token_red_url+"/login_push")

    userinfo = get_userinfo(token)
    if not userinfo:
        return redirect(token_red_url+"/login_push")

    school = userinfo["schoolName"]
    student_id = userinfo["userName"]
    name = userinfo["displayName"]
    mobile = userinfo["mobile"]
    data = {
        "token": token,
        "mobile": mobile,
        "school_name": school,
        "student_id": student_id,
        "name": name
    }

    return render_template("login_push.html", **data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    token = request.args.get('token')
    if not token:
        return render_template("login.html", token=token)

    authorization = get_authorization(token)
    if not authorization:
        return redirect(token_red_url)
    user = get_userinfo(token)
    print(user)
    name = user["nickName"]
    return render_template("login.html", token=token, name=name)





@app.route('/home', methods=['POST'])
def home():
    receive_token = request.form.get("token")
    receive_mobile = request.form.get("mobile")
    receive_school_name = request.form.get("school_name")
    receive_student_id = request.form.get("studentId")
    receive_username = request.form.get("username")
    data = {
        "school_name": receive_school_name,
        "username": receive_username,
        "mobile": receive_mobile,
        "token": [receive_token],
        "student_id": receive_student_id,
    }

    # 判断用户是否存在
    exists = False
    for course in user_data_list:
        if course["student_id"] == receive_student_id:

            if not receive_token in course["token"]:
                print("不在里面")
                course["token"].append(receive_token)
            else:
                print("在里面了")

            exists = True
            break  # 找到直接跳出循环，不用继续遍历

    if not exists:
        user_data_list.append(data)
    with open(f"DATA/userinfo{time.time()}.json", "w", encoding="utf-8") as f:
        json.dump(user_data_list, f, ensure_ascii=False, indent=4)
    # print(user_data_list)




    authorization = get_authorization(receive_token)

    course_list =  get_classroom_list(authorization, 100)

    # print(course_list)
    return render_template(
        "home.html",
        token=receive_token,
        authorization=authorization,
        course_list=course_list
    )
    ...


@app.route('/course/detail', methods=['POST'])
def course_detail():
    """课程详情"""
    # print(request.form.to_dict())
    authorization = request.form.get("authorization")
    wy_id = request.form.get("course_id")
    lb = get_course_detail_list(authorization, wy_id)

    return render_template("course_detail.html", activity_list=lb, authorization=authorization)


@app.route('/QR_code/check_in', methods=['POST'])
def QR_code_check_in():
    """二维码签到"""
    print(request.form.to_dict())
    authorization = request.form.get("authorization")
    activity_id = request.form.get("activity_id")
    jg = scan_to_check_in(authorization, activity_id)
    print(jg)
    return "<h1>签到完成</h1><br><hr><h1>" + str(jg)+"</h2>"






# ================================ 启动服务 ================================
if __name__ == '__main__':
    # print(">> https://sso.icve.com.cn/sso/auth?mode=simple&source=2&redirect=http://localhost:8080/login")
    # print()

    print(f"https://icve.052024.xyz/login_push")
    app.run(host=HOST, port=PORT, debug=True)


