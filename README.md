# Gallery-App

### HomePage
![Diana](/static/images/sereenshot2.png)

### ImageView
![Diana](/static/images/sreen3.png)

### GalleryPage
![Diana](/static/images/screenshot1.png)


## Table of Content

+ [Description](#description)
+ [Behaviour Driven Development](#behaviour-driven-development)
+ [Installation Requirement](#Installation)
+ [Technology Used](#technology-used)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#authors-info)
+ [Live Link](#live-link)

## Description

<p>A photo album application that displays a variety of photos based on their location and categories. Also a user can view more details of the photo by a click.</p>

## Behaviour Driven Development

<p>

* A user can view different photos.
* A user can click on a single photo to expand it and also view the details of the photo.
* As user can search on different categories of photos.
* A user can copy a link to the photo to share with my friends
* A user can view photos on the location they were taken.

</p>

***
## Installation

* Open Terminal `ctrl+Alt+T`

* Git clone https://github.com/Dianakariuki/Gallery-App.git

or

* Git fork - Enter into your own repository and search-https://github.com/Dianakariuki/Gallery-App.git then click on fork to add
it on your own repository.

 Navigate into the cloned project. 
`cd Gallery-app`


* Create and activate the vitual Environment and install the from requirements.txt
`$ python3.8 -m virtualenv virtual`
`$ source virtual/bin/activate`
`$ pip install -r requirements.txt`

* Setting up environment variables

Create an `.env` and add the following.
```
SECRET_KEY='<Secret_key>'
DBNAME='tribune'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='<your-email>'
EMAIL_HOST_PASSWORD='<your-password>'

```

requirements from 
---
`requirements.txt`


* Start the Server to run the app
* `$ python3.8 manage.py runserver`

* Open [localhost:8000](#)
***


### Requirements

* Either a computer,phone,tablet or an Ipad

* An access to the Internet

* Python3

* Postgres

* virtualenv

*Pip

[Go Back to the top](#Gallery-app)

## Technology Used

* HTML 5 - which was used to build the structure of the pages.

* CSS - which was used to style the pages incuding the left aside navigation bar.


* Python/Flask - Which was used to build the web-applications and interactivity

* Postgresql - For the database

* Heroku - For deployment

## Reference

* LMS
* W3schools
* stackOverFlow

[Go Back to the top](#Gallery-app)

## Licence

MIT License

Copyright (c) [2022](#licence) [Dianakariuki](#licence)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Go Back to the top](#Gallery-App)

## Authors Info



Gmail - [dianakariuki842@gmail.com]()

Github - [Dianakariuki](https://github.com/Dianakariuki)

## Live Link

LiveLink- (https://diana-gallery.herokuapp.com/)

[Go Back to the top](#Gallery-App)
