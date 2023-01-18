from flask import Flask, render_template, url_for, redirect, request
from flask_mail import Mail, Message
from config import mail_password, mail_username

app = Flask(__name__, static_folder="static")


app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)


@app.route("/")

@app.route("/home") 
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')    

@app.route("/portfolio") 
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog')    

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        Name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject=f"Mail from {Name}", body=f" Name: {Name}\n E-Mail: {email}\n\n\n{message}", sender="dssummers2424@gmail.com", recipients=['dhanushree0424@gmail.com'])
        mail.send(msg)
        return render_template("contact.html", success=True)

    return render_template('contact.html', title='contact')    

@app.route("/blogpost1")
def blogpost1():
    return render_template('blogpost1.html', title='BlogPost')    

@app.route("/login")
def login():
    return render_template('login.html', title='login')

@app.route("/signup")
def login():
    return render_template('signup.html', title='signup')    