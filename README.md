# politico-server
[![Build Status](https://travis-ci.org/Nduhiu17/politico-server.svg?branch=develop)](https://travis-ci.org/Nduhiu17/politico-server)
[![Coverage Status](https://coveralls.io/repos/github/Nduhiu17/politico-server/badge.svg?branch=develop)](https://coveralls.io/github/Nduhiu17/politico-server?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/8a586e40d862cd81b0e8/maintainability)](https://codeclimate.com/github/Nduhiu17/politico-server/maintainability)

### Description
Politico enables citizens give their mandate to politicians running for different government offices  while building trust in the process through transparency.

### Development
This Application is developed using python pure [Flask](http://flask.pocoo.org/docs/1.0/).The data is stored on python data structures


### Documentation Link
Please click [challenge two](https://politicoserver.docs.apiary.io/) to view challenge two api documentation

Please click [challenge three](https://politico-api-server.herokuapp.com/) to view challenge two api documentation

### Git hub Link
Please click [Github Link](https://github.com/Nduhiu17/politico-server/tree/develop) to view api the hosted source code on github.


### Endpoints

| METHOD | ENDPOINT                                            | DESCRIPTION                         |
| ------ | ---------------------------------------------       | --------------------------------    |
| POST   | /api/v1/parties                                     |End point to create a party          |
| GET    | /api/v1/parties                                     | Endpoint to get all parties         |
| GET    | /api/v1/parties/<int:partyid>                       | End point to get a specific political party|
| DELETE    | /api/v1/parties/<int:partyid>                    | Delete a specific party             |
| PATCH    | /api/v1/parties/<int:partyid>/name                 | Update a specific party name             |
| GET    | /api/v1/offices                | Get all offices      |
| POST   | /api/v1/offices       | Post an office        |
| GET    | /api/v1/offices/<int:officeid>    | Get a specific office          |

### Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python web microframework)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)
- [Pylint](https://www.pylint.org/) (Linting library)
- [Pip3](https://pypi.org/project/pip/) (Python package installer)


### Getting Started:

**To start the app, please follow the instructions below:**

**On your terminal:**

Install pip:
Install
Install sudo apt-get install python-pip
Install
- Clone this repository:

        $ git clone https://github.com/Nduhiu17/politico-server.git

- Get into the root directory:

        $ cd politico-server/

- Install virtual enviroment:

        $ python3.6 -m venv virtual

- Activate the virtual environment:

        $ source virtual/bin/activate
  
- Install requirements

        $ pip install -r requirements.txt

-Export server's secret key by:
        $ export SECRET_KEY='set-your-secret-key-here'

- Run the server by:

        $ python manage.py server

### Running the tests

Export server's secret key to the environment by:
     $ export SECRET_KEY='set-your-secret-key-here'


Run the tests by:

    $ pytest

# VERSION TWO

### Endpoints

| METHOD | ENDPOINT                                            | DESCRIPTION                         |
| ------ | ---------------------------------------------       | --------------------------------    |
| POST   | /api/v2/auth/signup                                 |End point to register a user         |
| POST   | /api/v2/auth/login                                  | Endpoint to login a user            |
| GET    | /api/v2/parties                                     | End point to get all parties        |
| POST   | /api/v2/parties                                     | End point to post a party           |
| GET    | /api/v2/parties/<int:id>                            | End point to get a party by id      |
| GET    | /api/v2/offices                                     | End point to get all offices        |
| POST   | /api/v2/offices                                     | End point to create an office       |
| GET    | /api/v2/office/<int:id>                             | End point to get an office by id    |
| POST   | /api/v2//office/<office-id>/register                | End point to register a candidate   |
| POST   | /api/v2/votes                                       | End point to vote for a candidate   |
| POST   | /api/v2//office/<office-id>/result                  | End point to get results for a election   |
| POST   | /api/v2/applications                                | End point to apply for candidature  |
| POST   | /api/v2/petitions                                   | End point to create a petition      |



#1## Getting Started with version two:

**To start the app, please follow the instructions below:**

**On your terminal:**

Install pip:
Install
Install sudo apt-get install python-pip
Install
- Clone this repository:

        $ git clone https://github.com/Nduhiu17/politico-server.git

- Get into the root directory:

        $ cd politico-server/

- Install virtual enviroment:

        $ python3.6 -m venv virtual

- Activate the virtual environment:

        $ source virtual/bin/activate
  
- Install requirements

        $ pip install -r requirements.txt

- Create postgress databases by running the following commands:

        $ psql

        $ CREATE DATABASE yourdbname WITH PASSWORD yourpassword

        $ CREATE DATABASE yourtestdbname WITH PASSWORD yourpassword

-Export server's secret key by:

        $ export SECRET_KEY='set-your-secret-key-here'

-Export server's JWT SECRET KEY by:

        $ export JWT_SECRET_KEY='set-your-secret-key-here'

-Export server's DATABASE URL by:

        $ export DATABASE_URL='postgres://yourdbusername:yourdbpassword@localhost:5432/yourdbname'


- Run the server by:

        $ python manage.py server

### Running the tests

-Export server's secret key to the environment by:

        $ export SECRET_KEY='set-your-secret-key-here'

-Export server's JWT SECRET KEY by:

        $ export JWT_SECRET_KEY='set-your-secret-key-here'

-Export test DATABASE URL by:

        $ export DATABASE_URL='postgres://yourdbusername:yourdbpassword@localhost:5432/yourtestdbname'


Run the tests by:

         $ pytest

### Author
Antony Mundia