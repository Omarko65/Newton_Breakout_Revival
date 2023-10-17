# Newton Breakout Revival API

**Version**: 1.0

## Introduction

This document provides an overview of the Newton Breakout Revival API. The API offers various endpoints to perform actions such as signin, signup, add scores, retrieve scores and other functionalities in the Newton Breakout Revival app
The Newton Breakout Revival is a mobile gaming APK
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
     - [Clone The Repository](#clone-the-repository)
     - [Install Dependencies](#install-the-dependencies)
  - [Usage](#usage)
- [API Endpoints](#api-endpoints)


## Features

All API endpoints are meant for the Newton Breakout Revival developers

## Technologies Used

Utilizes technologies like Python, Flask, SQLAlchemy, and more.

## Getting Started

### Prerequisites
#### Clone The Repository

To get started with the local development environment, clone the repository:

```bash
$ git clone https://github.com/holic65/Newton_Breakout_Revival.git
$ cd Newton_Breakout_Revival
```

#### Install Dependencies

You can set up the environment using either `venv` or `pipenv`. Here are instructions for both:

Using `venv`:

```bash
# create Virtual Environment
$ python3 -m venv venv

# Activate Virtual Env
$ source venv/bin/activate

# Install Dependencies
$ pip install -r requirements.txt
```

Using `pipenv`:

```bash
$ pip install pipenv

# create virtuel environment
$ pipenv --python 3.10

# Activate virtual env
$ pipenv shell

# install dependencies in requirements.txt or pipfile
$ pipenv install
```


### Usage

```bash
$ python3 run.py
```

## API Endpoints

### [https://newtonbreakoutrevival.onrender.com](#https://newtonbreakoutrevival.onrender.com)

#### `/game/signup`

- **POST**: Create a new user
  - **Summary**: Create a new user 
  - **Parameters**:
    - Request body as json
      - `name` (Required, string): Unique name of the user
      - `email` (Required, string): Unique email of the user
      - `Password` (Required, string): Password of the user
  - **Responses**:
    - `201`: User created successfully
      - success: True
      - name: "name of user"
      - email: "email of user"
    - `400`: Email or name already exist or Invalid email or name
      - success: False
      - message: Email or name already exist or Invalid email or name
    - `404`: An Error occurred
      - success: False
      - message: An error occurred 
    - `500`: Internal Server Error

#### `/game/signin`

- **POST**: Signin to an existing account
  - **Summary**: Signin to an existing account 
  - **Parameters**:
    - Request body as json
      - `email` (Required, string): Unique email of the user
      - `Password` (Required, string): Password of the user
  - **Responses**:
    - `200`: User sign-in successfully
      - success: True
      - name: "name of user"
      - email: "email of user"
    - `400`: Invalid email or password
      - success: False
      - message: Email does not exist or Incorrect password
    - `404`: An error occurred
      - success: False
      - message: An error occured 
    - `500`: Internal Server Error
      
   
#### `/game/guest`

- **POST**: Signin as a guest
  - **Summary**: Signin as a guest with just name 
  - **Parameters**:
    - Request body as json
      - `name` (Required, string): Name of the user
  - **Responses**:
    - `200`: User sign-in successfully
      - success: True
      - name: "name of user"
    - `400`: Invalid name
      - success: False
      - message: Enter a valid name
    - `404`: An error occurred
      - success: False
      - message: An error occured 
    - `500`: Internal Server Error

 
#### `/game/scoreboard`

- **POST**: Saves user's score to server 
  - **Summary**: Save user's score to server 
  - **Parameters**:
    - Request body as json
      - `name` (Required, string): Name of the user
      - `score` (Required, integer): User's score
  - **Responses**:
    - `200`: Score saved successfully
      - success: True
      - name: "name of user"
      - user_id: "user's id"
      - score: score
    - `400`: Invalid user
      - success: False
      - message: 'user does not exist'
    - `404`: An error occurred
      - success: False
      - message: An error occured 
    - `500`: Internal Server Error
   

#### `/game/scoreboard`

- **GET**: Get top 20 scores  
  - **Summary**: Get top 20 scores 
  - **Parameters**:
    - No parameters needed
  - **Responses**:
    - `200`: Scores returned successfully
      - [
          {
            'name': user's name,
            'score': user's score
          }
        ]
    - `404`: An error occurred
      - success: False
      - message: An error occured 
    - `500`: Internal Server Error
   

#### `/game/scoreboard/tournament`

  - **POST**: Saves score for tournament to server 
    - **Summary**: Save score for tournament to server 
    - **Parameters**:
      - Request body as json
        - `name` (Required, string): Name of the user
        - `score` (Required, integer): User's score
  - **Responses**:
    - `200`: Score saved successfully
      - success: True
      - name: "name of user"
      - user_id: "user's id"
      - score: score
    - `400`: Invalid user
      - success: False
      - message: 'user does not exist'
    - `404`: An error occurred
      - success: False
      - message: An error occured 
    - `500`: Internal Server Error
   

#### `/game/scoreboard/tournament`

- **GET**: Get top 20 scores in tournament
  - **Summary**: Get top 20 scores in tournament
  - **Parameters**:
    - No parameters needed
  - **Responses**:
    - `200`: Scores returned successfully
      - [
          {
            'name': user's name,
            'score': user's score
          }
        ]
    - `404`: An error occurred
      - success: False
      - message: An error occured 
    - `500`: Internal Server Error
