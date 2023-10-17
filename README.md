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
      - `name` (Required, string): Password of the user
  - **Responses**:
    - `201`: User created successfully
      - success: True
      - name: "name of user"
      - email: "email of user"
    - `400`: Email or name already exist
      - success: False
      - message: Email or name already exist
    - `404`: Invalid Error
      - success: False
      - message: Invalid Email or name 
    - `500`: Internal Server Error
