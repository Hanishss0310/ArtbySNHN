from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# Route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Check if all fields are filled
        if not name or not email or not message:
            flash('All fields are required!')
            return redirect(url_for('contact'))
        
        # Send email or save the message (using SMTP for this example)
        try:
            send_email(name, email, message)
            flash('Message sent successfully!')
        except Exception as e:
            flash('Failed to send message. Please try again later.')
            print(f"Error: {e}")
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

def send_email(name, email, message):
    # Email settings
    sender_email = 'your_email@example.com'
    receiver_email = 'receiver_email@example.com'
    password = 'your_email_password'

    # Compose the email
    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()  # Encrypt the email
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)
