from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = 'KISanBazaar212213@&@'  # Replace with your own secret key

# Configuring Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # e.g., smtp.gmail.com
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'kisanbazaar9@gmail.com'
app.config['MAIL_PASSWORD'] = 'hwdr ybgw rbcw zppe'

mail = Mail(app)


# Route for the home page
@app.route('/')
def home():
    signed_up = session.get('signed_up', False)
    return render_template('index.html', signed_up=signed_up)


# Route for handling the email sign-up
@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']

    if not email:
        flash('Email is required!', 'error')
        return redirect(url_for('home'))

    # Here you would typically save the email to your database
    # For simplicity, we are just printing it
    print(f"Received email: {email}")

    # Sending the confirmation email
    msg = Message('Welcome to Kisan Bazaar', sender='kisanbazaar9@gmail.com', recipients=[email])
    msg.body = f"Thank you for signing up, {email}! You are now registered with Kisan Bazaar."
    mail.send(msg)

    session['signed_up'] = True

    flash('You have successfully signed up! A confirmation email has been sent.', 'success')
    return redirect(url_for('home'))

@app.route('/submit-query', methods=['POST'])
def submit_query():
    name = request.form['name']
    email = request.form['email']
    query = request.form['query']

    if not (name and email and query):
        flash('All fields are required!', 'error')
        return redirect(url_for('home'))

    # Sending the contact form email
    msg = Message('New Order Query', sender=email, recipients=['kisanbazaar9@gmail.com'])
    msg.body = f"New query received from {name} ({email}):\n\n{query}"
    mail.send(msg)

    flash('Your query has been submitted successfully!', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
