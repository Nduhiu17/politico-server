# politico-server
[![Build Status](https://travis-ci.org/Nduhiu17/politico-server.svg?branch=develop)](https://travis-ci.org/Nduhiu17/politico-server)
[![Coverage Status](https://coveralls.io/repos/github/Nduhiu17/politico-server/badge.svg?branch=develop)](https://coveralls.io/github/Nduhiu17/politico-server?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/8a586e40d862cd81b0e8/maintainability)](https://codeclimate.com/github/Nduhiu17/politico-server/maintainability)

### Description
Politico enables citizens give their mandate to politicians running for different government offices  while building trust in the process through transparency.

### Development
This Application is developed using python pure [Flask](http://flask.pocoo.org/docs/1.0/).The data is stored on python data structures

Please click [Heroku Link](https://politico-version1.herokuapp.com/) to view api documentation and heroku api link

Please click [Github Link](https://github.com/Nduhiu17/politico-server/tree/develop) to view api the hosted source code on github.


#### Endpoints

| METHOD | ENDPOINT                                            | DESCRIPTION                         |
| ------ | ---------------------------------------------       | --------------------------------    |
| POST   | /api/v1/parties                                 |End point to create a party       |
| POST   | /api/v1/parties                                  | Endpoint to get all parties       |
| Get   | /api/v1/parties<int:partyid>                                   | End point to get a specific political party               |
| DELETE    | /api/v1/parties<int:partyid>                                   | Delete a specific party                 |
| PATCH    | /api/v1/parties/<int:partyid>/name                 | Update a specific party name             |
| GET    | /api/v1/offices                | Get all offices      |
| POST   | /api/v1/offices       | Post an office        |
| GET    | /api/v1/offices/<int:officeid>    | Get a specific office          |
