from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from email.message import EmailMessage

            
import smtplib
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abobabrat'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_users.db'
# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)


@app.route('/') 
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/sign-up')
def register():
    return render_template("sign-up.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/mail')
def mail():
    return render_template("mail.html")


@app.route('/services')
def services():
    return render_template("services.html")


@app.route('/single')
def single():
    return render_template("single.html")


@app.route("/api/forma/", methods=['POST', "GET"])
def post_api_form():
    data = request.get_data()
    print(data)
    # данные для отправки письма
    sender_email = 'sale@amlayn.ru'
    sender_password = 'SVzxPegQnGyCjL2HQH97'
    receiver_email = 'sale@amlayn.ru'
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    subject = 'Заявка на логистику'
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    body = f'Имя - {data_dict["name"]}\Почта - {data_dict["mail"]}\nНомер телефона - {data_dict["tel"]}\nТема - {data_dict["subject"]}\nПисьмо - {data_dict["message"]}'
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)
    server.sendmail(sender_email, receiver_email, msg.as_bytes())

    server.quit()
    return jsonify({"status": True})
    


if __name__ == "__main__":
    app.run(debug=True)





