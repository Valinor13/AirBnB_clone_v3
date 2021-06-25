# AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_amenity(self)` - Test that models/amenity.py conforms to PEP8
* `def test_pep8_conformance_test_amenity(self)` - Test that tests/test_models/test_amenity.py conforms to PEP8
* `def test_amenity_module_docstring(self)` - Test for the amenity.py module docstring
* `def test_amenity_class_docstring(self)` - Test for the Amenity class docstring

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_city(self)` - Test that models/city.py conforms to PEP8
* `def test_pep8_conformance_test_city(self)` - Test that tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Test for the city.py module docstring
* `def test_city_class_docstring(self)` - Test for the City class docstring

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_file_storage(self)` - Test that models/file_storage.py conforms to PEP8
* `def test_pep8_conformance_test_file_storage(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8
* `def test_file_storage_module_docstring(self)` - Test for the file_storage.py module docstring
* `def test_file_storage_class_docstring(self)` - Test for the FileStorage class docstring

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlaceDoc class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_place(self)` - Test that models/place.py conforms to PEP8.
* `def test_pep8_conformance_test_place(self)` - Test that tests/test_models/test_place.py conforms to PEP8.
* `def test_place_module_docstring(self)` - Test for the place.py module docstring
* `def test_place_class_docstring(self)` - Test for the Place class docstring

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReviewDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_review(self)` - Test that models/review.py conforms to PEP8
* `def test_pep8_conformance_test_review(self)` - Test that tests/test_models/test_review.py conforms to PEP8
* `def test_review_module_docstring(self)` - Test for the review.py module docstring
* `def test_review_class_docstring(self)` - Test for the Review class docstring

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestStateDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_state(self)` - Test that models/state.py conforms to PEP8
* `def test_pep8_conformance_test_state(self)` - Test that tests/test_models/test_state.py conforms to PEP8
* `def test_state_module_docstring(self)` - Test for the state.py module docstring
* `def test_state_class_docstring(self)` - Test for the State class docstring

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_user(self)` - Test that models/user.py conforms to PEP8
* `def test_pep8_conformance_test_user(self)` - Test that tests/test_models/test_user.py conforms to PEP8
* `def test_user_module_docstring(self)` - Test for the user.py module docstring
* `def test_user_class_docstring(self)` - Test for the User class docstring


## Examples of use

### Console

```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```
## API

Updates were made to the program to include a RESTful API that helps seamlessly integrate FileStorage and DBStorage with our front end HTML. 

Make sure on your machine that you have MySQL running, as well that your MySQL is set up with the appropriate user, password, databases, tables, and content.

## Spin up your server in this way:
``` 
root@0639522cfac7:/AirBnB_clone_v3# HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:588: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
  cursor.execute(statement, parameters)
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:588: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
  cursor.execute(statement, parameters)
 * Debugger is active!
 * Debugger PIN: 670-419-348
```
When your see '* Running on http://0.0.00:5000/ (Press CTRL+C to quit)" your server is active and ready to be tested.

## Testing the API

Below is usage on the command line to test that an instance of a Class object is is being manipulated in the desired way via the HTTP methods provided in the API code.

## GET all State instances the database in this way:

``` 
root@0639522cfac7:/AirBnB_clone_v3# curl -X GET http://0.0.0.0:5000/api/v1/states/
[
  {
    "__class__": "State",
    "created_at": "2017-03-25T02:17:06.000000",
    "id": "0e391e25-dd3a-45f4-bce3-4d1dea83f3c7",
    "name": "Alabama",
    "updated_at": "2017-03-25T02:17:06.000000"
  },
  {
    "__class__": "State",
    "created_at": "2017-03-25T02:17:06.000000",
    "id": "10098698-bace-4bfb-8c0a-6bae0f7f5b8f",
    "name": "Oregon",
    "updated_at": "2017-03-25T02:17:06.000000"
  }, 
  ....
```

## GET an instance of a specific State instance in this way:

```
root@0639522cfac7:/AirBnB_clone_v3# curl -X GET http://0.0.0.0:5000/api/v1/states/541bba6e-9543-4b33-8062-77ef26cd9778
{
  "__class__": "State",
  "created_at": "2017-03-25T02:17:06.000000",
  "id": "541bba6e-9543-4b33-8062-77ef26cd9778",
  "name": "Hawaii",
  "updated_at": "2017-03-25T02:17:06.000000"
}
```

## POST (create) a new instance of a class object in this way:

```
root@0639522cfac7:/AirBnB_clone_v3# curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "Oklahoma"}' -vvv
* Hostname was NOT found in DNS cache
*   Trying 0.0.0.0...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/states/ HTTP/1.1
> User-Agent: curl/7.35.0
> Host: 0.0.0.0:5000
> Accept: */*
> Content-Type: application/json
> Content-Length: 20
>
* upload completely sent off: 20 out of 20 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 193
< Access-Control-Allow-Origin: 0.0.0.0
< Server: Werkzeug/0.16.1 Python/3.4.3
< Date: Fri, 25 Jun 2021 20:59:12 GMT
<
{
  "__class__": "State",
  "created_at": "2021-06-25T20:59:12.757014",
  "id": "1810f786-b98a-4edb-b7a8-16b4f306f614",
  "name": "Oklahoma",
  "updated_at": "2021-06-25T20:59:12.757160"
}
* Closing connection 0
```
## PUT (udpate) an existing instance of a class object in this way:
```
root@0639522cfac7:/AirBnB_clone_v3# curl -X PUT http://0.0.0.0:5000/api/v1/states/1810f786-b98a-4edb-b7a8-16b4f306f614 -H "Content-Type: application/json" -d '{"name": "Kansas"}'

# updates the state id previously associated with "Oklahoma"

{
  "__class__": "State",  
  "created_at": "2021-06-25T20:59:13.000000",
  "id": "1810f786-b98a-4edb-b7a8-16b4f306f614",
  "name": "Kansas",
  "updated_at": "2021-06-25T21:03:10.218507"
}

```
## DELETE an object instance in this way:
```
root@0639522cfac7:/AirBnB_clone_v3# curl -X DELETE http://0.0.0.0:5000/api/v1/states/1810f786-b98a-4edb-b7a8-16b4f306f614
{}

```

## confirm that the DELETE worked successfully in this way:
```
root@0639522cfac7:/AirBnB_clone_v3# curl -X GET http://0.0.0.0:5000/api/v1/states/1810f786-b98a-4edb-b7a8-16b4f306f614
{
  "error": "Not found"
}
```





## Bugs
No known bugs at this time. 

## Authors
Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)  
Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)

**Holberton School 0x05 - RESTful API** Project Collaborators  
Jay Calhoun - [E-mail](jwcalhoun2@gmail.com)    
Nikki Edmonds - [E-mail](2495@holbertonschool.com)  
Chris Vanndy - [E-mail](chrisvannyc@gmail.com)


Second part of Airbnb: Joann Vuong
## License
Public Domain. No copy write protection. 
