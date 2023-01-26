# communication_ltd

![image](https://user-images.githubusercontent.com/34675746/212680091-d3bc2fd8-1b4b-454f-a6bf-d47298efb760.png)


This site is a project created as a part of the course "Computer Security"  of HIT (Holon Institute of Technology)
This is the web system, developed for an imaginary communication company called Communication_LTD,  sells Internet packages.
The site is used by customers, to buy or upgrade their internet plan.


Go to "Signup" to register new account, or press "Login" if account already exists.\
![image](https://user-images.githubusercontent.com/34675746/214829695-aa0b15b7-3f92-4078-a29a-7219dd03fb91.png)
![image](https://user-images.githubusercontent.com/34675746/214831648-98d715c7-552e-46d1-990e-775277337e43.png)

When You logged in, you can to buy new or update current internt plan\
![image](https://user-images.githubusercontent.com/34675746/214834422-93e67f3d-b91a-4f7d-ad3e-ca4077a49cf1.png)

 
 Only Registered user can send "Contact Us" form\
![image](https://user-images.githubusercontent.com/34675746/214833306-a853651f-aad0-4a9e-b853-74786fe41152.png)


### Installing
- If You do not have python, You can go to https://www.python.org/downloads/ to download th latest version

- create virtual environment: \
$ pip install --upgrade virtualenv \
$ virtualenv env 


- Install requirements: \
(env) $ pip install -r requirements.txt

- Make migrations:\
(env) $ python manage.py makemigrations \
(env) $ python manage.py migrate 

- as well, make also migrations separately to each app (here is 2): \
(env) $ python manage.py makemigrations order\
(env) $ python manage.py migrate order\
(env) $ python manage.py makemigrations users\
(env) $ python manage.py migrate users


- create superuser for admin login: \
(env) $ python manage.py createsuperuser 


## Running 
- to run server: \
$ python manage.py createsuperuser  

- to run over HTTPS: \
$ python manage.py runsslserver --certificate cert.pem --key key.pem 

## Admin panel
 - If You need to access to the site admin panel:\
 go to file "settings.py", and set parameter "DEBUG = True"  


## Authors
Vladimir Poplavsky https://github.com/VladimirPoplavsky \
Shaun Suhareanu https://github.com/Botnim \
Daniel Gardashnik https://github.com/Danielgard10 \
Valeria Zagorchik https://github.com/Vale-Za \
Ilya Yaverbaum https://github.com/ilyayaver95 

