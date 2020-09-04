Phone Verification Demo
=======================
Read the [blog Post](https://medium.com/@EphraimBuddy/building-a-real-world-phone-verification-api-endpoints-with-django-rest-framework-839c5e8ffb0b)

A phone number verification API tutorial

This app is to demonstrate how to create API endpoints for phone number verifications using Twilio SMS and pyotp in Django rest framework

To run this app on your system. Do the following:

### How to Run the app

```git clone https://github.com/ephraimbuddy/verify.git```

Change directory into the app:

```cd verify```

Create a new virtual environment

```python -m venv env```

Activate the environment

```source env/bin/activate``` On windows: ```source env\Scripts\activate```

Now install the necessary dependencies:

```pip install django djangorestframework twilio pyotp python-decouple```

Update the settings file:
First you need to signup with twilio to get your accound sd, token and phone number. After you get those things.
Create a `.env` file at the root of this app and add the twilio settings below:

    TWILIO_PHONE = your twilio phone number
    TWILIO_ACCOUNT_SID = your twilio account sid
    TWILIO_AUTH_TOKEN = your twilio auth token

After installation, run the migration:

```python manage.py makemigrations```
```python manage.py migrate```

Create super user:

```python manage.py createsuperuser```

Run the App:
```python manage.py runserver```

### Endpoints:

    ^users/$ [name='user-list']
    ^users/(?P<pk>[^/.]+)/$ [name='user-detail']
    send_sms_code/
    verify_phone/<int:sms_code>
    ^phones/$ [name='phonenumber-list']
    ^phones/(?P<pk>[^/.]+)/$ [name='phonenumber-detail']
    api-auth/
    
Navigate to `http://127.0.0.1:8000/users/`.
Login and update the phone number. After you have saved it, head to `http://127.0.0.1:8000/send_sms_code/` and an sms will be sent to your phone. Use the code sent to form the verify_phone url: `http://127.0.0.1:8000/verfiy_phone/your_code_here`.

###The end
