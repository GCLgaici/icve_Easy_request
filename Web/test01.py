from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "abc123456"

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ""
    class_val = ""
    # 后端生成/读取token，传给页面
    token = "admin-2026-token-xyz123456"

    if request.method == "POST":
        name = request.form.get("username")
        class_val = request.form.get("className")
        receive_token = request.form.get("token")  # 接收前端带回的token
        print("表单携带的Token：", receive_token)

        if name and class_val:
            print(f"提交成功！姓名：{name}，班级：{class_val}")
        else:
            print("姓名和班级不能为空！")

    # 把token传入模板
    return render_template("test01_index.html", name=name, class_val=class_val, token=token)

if __name__ == '__main__':
    app.run(debug=True)