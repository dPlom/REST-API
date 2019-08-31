# REST API

This API can recive a *user_id* and return his information. 
If the *user_id* is missing you'll receive an error.

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
* Python: Enter https://www.python.org/downloads/ and download the 3.7.4 version. 

  Run and install it.
* Flask: *pip install Flask*

## Running the test
Make a POST request with a json object that contains a user_id.

```
{
'user_id':'123'
}
```


This ID should return:
```
 {
  "user": {
    "Address": {
      "city": "reipå - oslo",
      "street": "ole jacob brochs gate 1992"
    },
    "firstname": "pelle",
    "image": "https://randomuser.me/api/portraits/med/men/60.jpg",
    "lastname": "mohammadi"
  }
}
```

## Built With
[Eclipse](https://www.eclipse.org)

[Postman](https://www.getpostman.com/)

## Authors
__Atilio Moretti__









