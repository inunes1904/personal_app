import smtplib
import requests as requests
from flask import Flask, render_template, request
import requests


app = Flask(__name__)

my_email = "inunes1904@yahoo.com"
password = "%;V9f(a9RR"+"'"+"f8)b"
app_password = "hzhffhhovbqbbpfr"


@app.route('/', methods=["GET", "POST"])
def index(name=None):
    if request.method == 'POST':
        form_info = request.form
        context = {item: form_info[item] for item in form_info}
        send_mail(context)
        return render_template('index.html', name=name)
    return render_template('index.html', name=name)


def send_mail(context):
    message = str(context['message'])
    client_mail = str(context['email'])
    subject_mail = str(context['subject'])
    person_name = str(context['name'])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="inunes1904@gmail.com",
            msg=f"Subject:{subject_mail.encode('ascii', 'ignore').decode('ascii')}\n\n"
                f"{message.encode('ascii', 'ignore').decode('ascii')}\n\n\n"
                f"To respond to the person use this email: {client_mail.encode('ascii', 'ignore').decode('ascii')}\n"
                f"The person name is: {person_name.encode('ascii', 'ignore').decode('ascii')}"
        )


