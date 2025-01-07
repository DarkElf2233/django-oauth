# Django Oauth

### An example of using django-oauth-toolkit in Django application.

## Step 1: Set up project

Clone repository and create virtual evironment using:
```
python -m venv .venv
```
And activate it:
```
.\.venv\Scripts\activate
```
Then install required packages:
```
pip install -r requirements.txt
```
Fill in .env file using .env.template and create a database.

## Step 2: Set up Oauth Provider

First apply migrations:
```
python manage.py migrate
```
And create super user:
```
python manage.py createsuperuser
```
Then run dev server:
```
python manage.py runserver
```
After that, follow the [route](http://127.0.0.1:8000/auth/applications/) and create a new application like on the [screenshot](https://github.com/DarkElf2233/django-oauth/blob/main/images/oauth_provider_create_application_example.png).

**Note: Don't forget to untick "Hash client secret" or you won't be able to get it later!**

After you created your application save client id and client secret to your **.env** file.

## Step 3: Test Oauth Provider

To run requests in **auth.http** file you need to insall **Rest Client Extension** in Visual Studion Code. Just go to **Extensions** tab and search "rest client" and install the first variant. 

After that,create a new file called "auth.http" fill it like in "auth.http.template". Don't forget place your variables in places marked with "<>". Then click on "Send Request" above requests to test Oauth Provider.

**Note: Your dev server must be started or it won't be able send requests!**