import ezgmail

try:
    ezgmail.init()
    print("SMTP login successful.")
except ezgmail.SMTPAuthenticationError:
    print("SMTP login failed. Check if Less secure app access is enabled.")
except Exception as e:
    print("An error occurred:", str(e))