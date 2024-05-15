import smtplib
import random
import time


Cooldown_Period = 60  # seconds

#track Last Email Sent

last_email_sent_time = 0


def generate_otp():
    # Generate a random 6-digit OTP
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def send_email_with_otp(email, otp):
    # Email configuration
    sender_email = 'miglopez23@gmail.com' 
    sender_password = 'mgarczpbrsckkejn' 
    smtp_server = 'smtp.gmail.com'  # Change this if using a different email provider
    smtp_port = 587  # Change this if using a different email provider

    
    # Construct the email message
    subject = 'Your OTP for Two-Step Verification'
    body = f'Your OTP (One Time Password) is: {otp}'
    message = f'Subject: {subject}\n\n{body}'

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to the SMTP server
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, email, message)

    

    # Close the connection
    server.quit()

    last_email_sent_time = time.time()

def verify_otp(opt_user_input, generated_otp):
    return opt_user_input == generated_otp


