Django Chat App
===================================



Quick start
-----------

1. Set you project directory
2. Clone the code from repository

   ```git clone <link>```
3. Set current working directory as "trade-master"

   ```cd chatapp```
4. set python virtualenv using below command

   ``` python3 -m venv env```
5. Activate python environment

       On Linux use
       ``` source env/bin/activate```
6. 
       On Windows use  
       ```source env\Scripts\activate```
6. Install or upgrade pip

   ```pip install --upgrade pip```
7. Install python packages/dependencies

   ```pip install -r requirements.txt```

8. Make and migrate database migrations
    ```
    python manage.py makemigrations
    python manage.py migrate 
    ```
9. Create User Account
    ```
    python manage.py createsuperuser
    ```
10. Run Django Development Server
    ```python manage.py runserver ```

Usage
-----------

1. Open your web browser and navigate to the URL http://localhost:8000/.
2. Click on the "LOGIN" button. If you haven't signed up yet, you can do so by clicking the "Sign Up" button.
3. Enter your credentials and sign in to your account.
4. Once signed in, click on the "CHAT" button to initiate a conversation with other users.
5. On the Chat Page, messages will be displayed every time a user sends a message.