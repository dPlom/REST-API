# REST API

This API can recive an *user_id* and return this information. If the *user_id* is missing you'll recive an error.

  - Lastname
  - Firstname
  - Profile Picture
  - Adrees:
    -Street
    -City and State

## Requirements
-Python 3.7.4
-Flask

## Installation
* Python: Enter https://www.python.org/downloads/ and download the 3.7.4 version. Run and install it.
* Flask: *pip install Flask*

## Running the test
Make a *json's POST request* that content a *json objet* with an user_id. You can obtain it from randomuser.me
```https://randomuser.me/api/?ud=%3Cid%3E```
This ID should return:
```
    - Lastname: grimsrud
    - Firstname: ali
    - Profile Picture:
    - Adrees: https://randomuser.me/api/portraits/med/men/18.jpg
        -Street: viggo hansteens vei 9905
        -City and State: sykkylven - bergen
```

## Built With
[Eclipse](https://www.eclipse.org)
[Postman](https://www.getpostman.com/)

## Authors
__Atilio Moretti__









