AirBnB Clone Project

**Description**
This project is a simplified clone of the AirBnB web application,
focusing on the backend functionality.
It includes a command interpreter to manage objects,
which is the foundation for building the front-end and web framework components.

**Command Interpreter**

How to Start It
To start the command interpreter, navigate to the project directory and run:
python3 console.py

How to Use It
The command interpreter allows you to create, read, update,
and delete objects. It supports various commands:

create <ClassName>: Creates a new instance of a class,
saves it to the JSON file, and prints the ID.
show <ClassName> <id>: Prints the string representation of an
instance based on the class name and ID.
destroy <ClassName> <id>: Deletes an instance based on the class name and ID.
all [<ClassName>]: Prints all string representations of all instances,
or instances of a specific class.
update <ClassName> <id> <attribute name> <attribute value>: 
Updates an instance based on the class name and ID by adding or updating an attribute.

Examples
(hbnb) create BaseModel
e79e8d46-812c-42f3-95f2-7df83f8c0c42
(hbnb) show BaseModel e79e8d46-812c-42f3-95f2-7df83f8c0c42
[BaseModel] (e79e8d46-812c-42f3-95f2-7df83f8c0c42)
 {'id': 'e79e8d46-812c-42f3-95f2-7df83f8c0c42', 'created_at':
 '2024-05-18T10:44:22.409202', 'updated_at': '2024-05-18T10:44:22.409222'}
(hbnb) destroy BaseModel e79e8d46-812c-42f3-95f2-7df83f8c0c42
(hbnb) all BaseModel
[]
(hbnb) update BaseModel e79e8d46-812c-42f3-95f2-7df83f8c0c42 name "My BaseModel"
(hbnb) show BaseModel e79e8d46-812c-42f3-95f2-7df83f8c0c42
[BaseModel] (e79e8d46-812c-42f3-95f2-7df83f8c0c42)
{'id': 'e79e8d46-812c-42f3-95f2-7df83f8c0c42', 'created_at': 
 '2024-05-18T10:44:22.409202', 'updated_at':
 '2024-05-18T10:44:22.409222', 'name': 'My BaseModel'}

Project Repository:
GitHub repository: AirBnB_clone

Anthor: Joshua Yamoah Yankson
