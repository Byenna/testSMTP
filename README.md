The `ezgmail` module requires a credentials file named `credentials.json` to authenticate with the Gmail API. This file contains the necessary information to authorize your application to access Gmail.

To resolve this issue, follow these steps:
1. Go to the Gmail API quickstart page: https://developers.google.com/gmail/api/quickstart/python
2. Click on the "Enable the Gmail API" button. This will walk you through the process of creating a new project and enabling the Gmail API for that project.
3. After enabling the API, you will be prompted to configure the OAuth consent screen. Choose the appropriate options and save your changes.
4. On the "Credentials" tab, click on the "Create credentials" button and select "OAuth client ID".
5. On the next page, select "Desktop app" as the application type and give it a name.
6. Click the "Create" button to generate the client ID and client secret.
7. Click on the "Download JSON" button next to your newly created credentials.
8. Save the downloaded JSON file to your project directory and rename it to `credentials.json`.
9. Now, try running your script again. The `ezgmail` module should be able to find the credentials file and authenticate with the Gmail API.
Make sure to import the `ezgmail` module and initialize it with the `init()` function before attempting to use any other functions. For example:
python
```
import ezgmail

try:
    ezgmail.init()
    print("SMTP login successful.")
except ezgmail.EZGmailException as e:
    print("SMTP login failed:", str(e))
```

With the correct `credentials.json` file in place, the `ezgmail` module should be able to authenticate successfully and interact with Gmail using SMTP.