# Flask Demo API
[![Python version](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Travis CI](https://travis-ci.org/Joffreybvn/challenge-flask-api.svg?branch=master)](https://travis-ci.org/github/Joffreybvn/challenge-flask-api/)

**Flask Demo API** is a RESTful API written in Python with Flask, for a challenge given by [Becode](https://becode.org/).

### Test the API with [Postman](https://www.postman.com/):
To start using this API, visit the Swagger documentation on:
 - v1: [http://flask-demo-api.herokuapp.com/v1/](http://flask-demo-api.herokuapp.com/v1/)
 - v2: [http://flask-demo-api.herokuapp.com/v2/](http://flask-demo-api.herokuapp.com/v2/)

# The challenge:
This API was created for me to learn some key concept and must-have features that modern API need to implement.

### Objectives
Create an API ready to deliver a machine learning model to customers: The API need to be able to receive data from the user, and deliver a result based on a ML model.

### Constraints:
 - Create a **REST** API.
 - Make the API **easy-to-use** to the end-user:
    * With full documentation.
    * With examples.
 - Make the API easily **scalable**:
    * Easy to add new features.
    * Easy to modify new features.<br>
    <img src="https://raw.githubusercontent.com/Joffreybvn/challenge-collecting-data/master/docs/arrow.svg" width="12"> While still being **backward-compatible**: Nothing have to break when a feature is added/reworked.
 - Implement **Continuous Integration** and **Continuous Deployment**.
 - Respect the [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/) whenever possible.
 - Write fully documented code (doctring), to improve maintainability.

### API structure:

    * By writing unit tests.
    * By using a CI-CD platform: [Travis CI](https://travis-ci.org/github/Joffreybvn/challenge-flask-api).
    * By creating a Docker Image and hosting it on [Heroku](https://heroku.com/).