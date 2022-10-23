# result_management

Create a project using django-admin and then set configuration. Add `.env` file inside folder where you can see `settings.py`. Genereate a random secret key using secret package from python and paste `SECRET_KEY` = "<<value>>" here.

First of all to connect to MySql database edit the credentials based on your configuration, then run `py manage.py makemigrations && py manage.py migrate`.
  

To get access of the admin panel run `py manage.py createsuperuser` command and now give enter a username as well as email*.

Now run `py manage.py runserver` command inside root folder. Now, I believe you can see the page in your default browsers.



Here's some screenshot of the output



## Student Data

![Screenshot 2022-10-23 221902](https://user-images.githubusercontent.com/47697392/197405039-5943d8f4-5ebd-4105-9752-2bf6e01d960f.png)

## Student result 

![Screenshot 2022-10-23 222003](https://user-images.githubusercontent.com/47697392/197405041-97a20448-398e-4689-94d5-4137ce533f77.png)
