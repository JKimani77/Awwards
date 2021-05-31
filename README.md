### PROJECT NAME
AWWARDS
### Author
Maryam Muchai
### Description
* The application allows a user to post a project he/she has created and get it reviewed by his/her peers.
### User Story
* Users need to Sign in to the application to post projects and review projects.
![Screenshot from 2021-05-31 23-15-05](https://user-images.githubusercontent.com/78798386/120239319-b2f84580-c266-11eb-9ecf-db3c8966c092.png)
* Users can view different projects and their details.
![Screenshot from 2021-05-31 23-23-30](https://user-images.githubusercontent.com/78798386/120239632-5a757800-c267-11eb-95b0-7e0e5b358224.png)
* Users can post a project to be rated/viewed.
![Screenshot from 2021-05-31 23-16-04](https://user-images.githubusercontent.com/78798386/120239498-184c3680-c267-11eb-97b8-d8ea515b8f1a.png)
* Users can search for different projects.

* Users can view projects overall score.

* Users can view their profile page with all their published projects.
![Screenshot from 2021-05-31 23-16-20](https://user-images.githubusercontent.com/78798386/120239396-dcb16c80-c266-11eb-8001-ee6900f78a20.png)
* Users can rate/review other users' projects.
![Screenshot from 2021-05-31 23-15-41](https://user-images.githubusercontent.com/78798386/120239448-f9e63b00-c266-11eb-9839-6a88b027e76c.png)
### Setup/Installation
1. Clone this repo: git clone 

2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer here.

4. To run the app, you'll have to run the following commands in your terminal

5. pip install -r requirements.txt
On your terminal,Create database awwards using the command below.
* CREATE DATABASE awwards; 

>if you opt to use your own database name, replace awwards your preferred name, then also update settings.py variable DATABASES > NAME

6.Migrate the database using the command below

>python3 manage.py migrate

7.Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

>python manage.py runserver

### Technologies Used
* Python3
* Django3
* Javascript
* Cloudinary
* Bootstrap
* HTML
* CSS
### APIs
This application comes with two API Endpoints for Profiles and Projects.

* Profiles API Endpoint - 

* Projects API Endpoint - 

### Contact Information
If you have any question or contributions, please email me at maryammuchai@gmail.com

### LICENSE
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

* Copyright(c)2021 Maryam Muchai
