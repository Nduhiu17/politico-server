# politico-server
[![Build Status](https://travis-ci.org/Nduhiu17/politico-server.svg?branch=develop)](https://travis-ci.org/Nduhiu17/politico-server)
[![Coverage Status](https://coveralls.io/repos/github/Nduhiu17/politico-server/badge.svg?branch=develop)](https://coveralls.io/github/Nduhiu17/politico-server?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/8a586e40d862cd81b0e8/maintainability)](https://codeclimate.com/github/Nduhiu17/politico-server/maintainability)

### Description
Politico enables citizens give their mandate to politicians running for different government offices  while building trust in the process through transparency.

### Development
This Application is developed using python pure [Flask](http://flask.pocoo.org/docs/1.0/).The data is stored on python data structures


### Heroku Link
Please click [Heroku Link](https://politico-version1.herokuapp.com/) to view api documentation and heroku api link

### Git hub Link
Please click [Github Link](https://github.com/Nduhiu17/politico-server/tree/develop) to view api the hosted source code on github.


### Endpoints

| METHOD | ENDPOINT                                            | DESCRIPTION                         |
| ------ | ---------------------------------------------       | --------------------------------    |
| POST   | /api/v1/parties                                 |End point to create a party       |
| GET   | /api/v1/parties                                  | Endpoint to get all parties       |
| GET   | /api/v1/parties/<int:partyid>                                   | End point to get a specific political party               |
| DELETE    | /api/v1/parties/<int:partyid>                                   | Delete a specific party                 |
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



- Run the app by:

        $ python manage.py server

### Running the tests

Export server's secret key to the environment by:
     $ export SECRET_KEY='set-your-secret-key-here'


Run the tests by:

    $ pytest

### Author
Antony Mundia