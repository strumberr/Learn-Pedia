from flask import Flask
from flask_mail import Mail, Message


app = Flask('')

mail = Mail()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'codertyper@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def emailsend(name, email, code, title, url):
   with app.app_context():
      msg = Message(f'Hello {name}', sender = 'codertyper@gmail.com', recipients = [f'{email}'])
      msg.subject = f"Hello {name}! From LearnPedia!"
      msg.html = f"""
      <div style="text-align: center;">
         <h1 style="font-weight: 500;">Good Day,</h1> 
         <div style="font-size: 40px; font-weight: 600;">{name}</div>
         <div style="font-size: 50px;">🥵</div>
         <h2 style="font-weight: 500;">Your deleting/editing code for the page:<h2>
         <div style="font-size: 30px; font-weight: 600;">{title}</div>
         <div style="font-size: 30px; font-weight: 500;">is:</div>
         <div style="font-size: 50px; font-weight: 600;">{code}</div>
         <h2 style="font-weight: 500;">Here is a link to your page!<h2>
         <h2 style="font-weight: 500;"><a href="{url}">Click here for your page!</a><h2>

         

         <br>
         <div style="font-weight: 500;">Please remember this code or keep it in your email. YOU CAN'T GET IT BACK IF IT GETS LOST!</div>
         <div>
      </div>
      """
      mail.send(msg)
      print("sent")
