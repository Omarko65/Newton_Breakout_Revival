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
      - `user_id` (Required, string): Id of the user
      - `score` (Required, integer): User's score
  - **Responses**:
    - `200`: Score saved successfully
      - success: True
      - name: "name of user"
      - user_id: "user's id"
      - score: score
      - score_id: score id,
      - message: 'Score updated successfully' || Score not updated     previous score is higher or equal' || 'Score added successfully'
    - `400`: Invalid user
      - success: False
      - message: 'user does not exist'
    - `404`: An error occurred
      - success: False
      - message: 'An error occured'
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
            'score': user's score,
            'score_id': score id
          }
        ]
    - `404`: An error occurred
      - success: False
      - message: An error occured 
    - `500`: Internal Server Error
   

#### `/game/scoreboard/<score_id>`
  - **DELETE**: Delete users from tournament scoreboard
     - **Summary**: Delete user score from tournament scoreboard
     - **Parameters**: No parameter needed
     - **Responses**:
      - `200`: Score deleted successfully
        - success: True
        - message: 'score deleted successfully
      - `400`: Invalid score
        - success: False
        - message: 'score not found'
      - `404`: An error occurred
        - success: False
        - message: An error occured 
      - `500`: Internal Server Error

#### `/game/scoreboard/tournament`

  - **POST**: Saves score for tournament to server 
    - **Summary**: Save score for tournament to server 
    - **Parameters**:
      - Request body as json
        - `user_id` (Required, string): Id of the user
        - `score` (Required, integer): User's score
  - **Responses**:
    - `200`: Score saved successfully
      - success: True
      - name: "name of user"
      - user_id: "user's id"
      - score: score
      - score_id: score id,
      - message: 'Score updated successfully' || Score not updated     previous score is higher or equal' || 'Score added successfully'
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
            'score': user's score,
            'score_id': score id
          }
        ]
    - `404`: An error occurred
      - success: False
      - message: An error occured 
    - `500`: Internal Server Error

#### `/game/scoreboard/tournament/<score_id>`
  - **DELETE**: Delete users score from tournament scoreboard
     - **Summary**: Delete user score from tournament scoreboard
     - **Parameters**: No parameter needed
    - **Responses**:
      - `200`: Score deleted successfully
        - success: True
        - message: 'score deleted successfully
      - `400`: Invalid score
        - success: False
        - message: 'score not found'
      - `404`: An error occurred
        - success: False
        - message: An error occured 
      - `500`: Internal Server Error




## Screenshots (Postman):

#### https://newtonbreakoutrevival.onrender.com/game/signup
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/7eca5d2d-597c-415a-a818-ea1176868ef0)



#### https://newtonbreakoutrevival.onrender.com/game/signin
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/c242dad0-2a2b-4a21-ba69-2460fb87e8f2)



#### https://newtonbreakoutrevival.onrender.com/game/guest
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/daa41ecf-65d2-408d-9164-8145783a37a4)



#### https://newtonbreakoutrevival.onrender.com/game/scoreboard [POST]
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/7b9d5a92-bdbc-4174-811a-3acc1789351d)



#### https://newtonbreakoutrevival.onrender.com/game/scoreboard [POST] (Only takes highest score)
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/535fddb2-e6ef-418d-ad67-28ee023e5891)




#### https://newtonbreakoutrevival.onrender.com/game/scoreboard [GET]
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/5db59cf9-5e51-4b41-9162-d63c10c92e45)



#### https://newtonbreakoutrevival.onrender.com/game/scoreboard [DELETE]
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/9777d837-d3c1-4b8f-a0ec-ed81fbddfd5e)




#### https://newtonbreakoutrevival.onrender.com/game/scoreboard/tournament [POST]
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/803dce56-c2ec-472c-9a62-b8aaefd63660)




#### https://newtonbreakoutrevival.onrender.com/game/scoreboard/tournament [POST] (Only takes highest score)
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/28e8fb71-2418-49b9-a69b-d064dbcee048)




#### https://newtonbreakoutrevival.onrender.com/game/scoreboard/tournament [GET]
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/3a7debfd-31ef-47ef-95cf-1d1a5ea35183)




#### https://newtonbreakoutrevival.onrender.com/game/scoreboard/tournament/<score_id> [DELETE]
![image](https://github.com/Holic65/Newton_Breakout_Revival/assets/56598437/e3600399-8857-4f0a-a978-3131c1c14fa9)



