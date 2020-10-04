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
 - Organize and **specify** the architecture of the API before any implementation.
 - Respect the [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/) whenever possible.
 - Write fully documented code (doctring), to improve maintainability.

# How to solve this challenge:

### 1. [Flask](https://flask.palletsprojects.com/) for a REST API
Flask is a small but powerful framework, **used to create small website and API**. It was chosen over Django because it is simpler, and let the developer choose the way he want to implement other services (eg: database).

### 2. Make it scalable and backward-compatible

#### Problem:
Creating a scalable API is not easy. Here is why:
> How to create an API that we will be able to modify/upgrade later, without breaking the compatibility with the software that were using the API ?

#### Solution:
The API will be composed of **multiple sub-module for each versions**:
 1. We create today a "*v1 module*" of the API.
 2. Later, to implement a huge modification that require to rewrite the routes, we'll create a "*v2 module*" in the API.

During a relatively long period of time, **both versions-module will be online**: To ensure that the applications that use the API will have time to implement the new version, without their services to stop working.
This way, the API is easily scalable and remains backward-compatible.

To achieve this, the [Blueprint](https://flask.palletsprojects.com/en/1.1.x/blueprints/) feature of Flask was used: it allow to divide a web app into smaller modular web app easily.

#### Structure of the API:
<p align="center">
    <img src="https://raw.githubusercontent.com/Joffreybvn/challenge-flask-api/master/doc/implementation.svg">
</p>

### 3. Write a fully documented API for the end-user

#### Problem:
**There is no API if there is no documentation.** A user need to know quickly how to interact with the API. Do do so, a clear documentation is needed.

#### Solution:
The library [Flask Restx](https://flask-restx.readthedocs.io/en/latest/) allow developers to quickly create a Swagger webpage with all documentation needed:
 - The structure of the **requests**.
 - The **routes**.
 - The structure of the **responses**.
 - A **script to test the API in the browser** !

Thanks to this library, writing the documentation was done while implementing the API. So that when a new route is created/edited, the **doc get immediately updated**.

See the doc: [http://flask-demo-api.herokuapp.com/v1/](http://flask-demo-api.herokuapp.com/v1/)

### 4. Before implementing: The specification

Implementing an API require to specify it. The "v1" of this API was build based on this chart, which define **the requests**, **the routes** and **the responses**:

<p align="center">
    <img src="https://raw.githubusercontent.com/Joffreybvn/challenge-flask-api/master/doc/structure.svg">
</p>

### 5. Implement PEP-8 documented code
As always, the implementation of this API follow the **[PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/)**, with a **fully documented code**. For example, take a look at [this chunk of code](https://github.com/Joffreybvn/challenge-flask-api/blob/master/api/v1/routes/status.py).

It enhance the code maintainability, and later modifications will be easier.

### 6. Continuous Integration
Tests were written to prevent any regression in the code. They can be found in [the *tests* folder](https://github.com/Joffreybvn/challenge-flask-api/tree/master/tests). The tests are executed on [Travis CI](https://travis-ci.org/), continuous integration and deployment platform.

### 7. Continuous Deployment
[Travis CI](https://travis-ci.org/) is also very useful for Continuous Deployment:
One pushed, the tests run, then:
 - A Docker image is created.
 - The image in uploaded to the Docker hub.
 - The image is pushed and executed to [Heroku](https://heroku.com/).

This way, everytime a new version is pushed, the Heroku app is automatically updated. The status of the last deployment is publicly visible on [this Travis repository](https://travis-ci.org/github/Joffreybvn/challenge-flask-api).

# About the Author
This challenge was solved in three days by [Joffrey Bienvenu](https://github.com/Joffreybvn), while studying Machine Learning @ [Becode](https://becode.org/).