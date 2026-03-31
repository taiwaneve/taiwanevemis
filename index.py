from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>楊子青Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><hr>"
    homepage += "<a href=/today>顯示日期時間</a><hr>"
    homepage += "<a href=/welcome?nick=tcyang>傳送使用者暱稱</a><hr>"
    homepage += "<a href=/account>網頁表單傳值</a><hr>"
    homepage += "<a href=/about>子青簡介網頁</a><hr>"
    homepage += "<a href=/welcome?u=子青&dep=靜宜資管>GET傳值</a><hr>"
    homepage += "<a href=/math>數學運算</a><hr>"
    homepage += "<a href=/cup>擲茭</a><hr>"
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1><a href=/>回到網站首面</a>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET"])
def welcome():
    x = request.values.get("u")
    y = request.values.get("dep")
    return render_template("welcome.html", name = x, dep = y)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/math", methods=["GET", "POST"])
def math():
    if request.method == "POST":
        # 取得使用者輸入的數值與運算子
        try:
            x = float(request.form.get("x"))
            y = float(request.form.get("y"))
            opt = request.form.get("opt")
            
            # 進行運算
            if opt == "+":
                result = x + y
            elif opt == "-":
                result = x - y
            elif opt == "*":
                result = x * y
            elif opt == "/":
                result = x / y if y != 0 else "除數不能為 0"
            else:
                result = "未知運算"
                
            return f"<h1>計算結果：{x} {opt} {y} = {result}</h1><a href='/math'>重新計算</a> | <a href='/'>回首頁</a>"
        except:
            return "<h1>輸入錯誤，請輸入數字！</h1><a href='/math'>重新嘗試</a>"
    else:
        return render_template("math.html")

@app.route('/cup', methods=["GET"])
def cup():
    # 檢查網址是否有 ?action=toss
    #action = request.args.get('action')
    action = request.values.get("action")
    result = None
    
    if action == 'toss':
        # 0 代表陽面，1 代表陰面
        x1 = random.randint(0, 1)
        x2 = random.randint(0, 1)
        
        # 判斷結果文字
        if x1 != x2:
            msg = "聖筊：表示神明允許、同意，或行事會順利。"
        elif x1 == 0:
            msg = "笑筊：表示神明一笑、不解，或者考慮中，行事狀況不明。"
        else:
            msg = "陰筊：表示神明否定、憤怒，或者不宜行事。"
            
        result = {
            "cup1": "/static/" + str(x1) + ".jpg",
            "cup2": "/static/" + str(x2) + ".jpg",
            "message": msg
        }
        
    return render_template('cup.html', result=result)


if __name__ == "__main__":
    app.run()
