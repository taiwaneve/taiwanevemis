from flask import Flask, render_template, request
from datetime import datetime

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

if __name__ == "__main__":
    app.run()
