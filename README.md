`pip3 install django`

`pip3 install djangorestframework`


`pip3 install django-cors-headers`

Create Django Project:
`django-admin startproject DjangoAPI`

`cd DjangoAPI`



### __init__.py
empty file that indicates this is a Python Project or a Python Module

### asgi.py
is the entry point for the ASGI compatible servers

### wsgi.py
is the entry point for the WSGI compatible servers

### asgi.py
is the entry point for the ASGI compatible servers

### urls.py
contains all the url declarations needed for this project

### settings.py
contains all the settings and config needed for this project

### manage.py
is a command line utility that helps interact with the Django Project


# run the project:
`python3 manage.py runserver`

#### server is now running:
```
Django version 4.1.7, using settings 'DjangoAPI.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


# create an App within the Django Project:
`python3 manage.py startapp EmployeeApp`


## modify 'settings.py' 
```
CORS_ORIGIN_ALLOW_ALL
CORS_ORIGIN_ALLOW_ALL=True
```
is not recommended in production, instead, listing the URL's to whitelist

`python3 manage.py migrate EmployeeApp`


```json
CREATE TABLE "EmployeeApp_departments" (
	"DepartmentId"	INTEGER NOT NULL,
	"DepartmentName" TEXT,
RIMARY KEY (departmentId)
```

```json
CREATE TABLE "EmployeeApp_employees" (
	"EmployeeId"	INTEGER NOT NULL,
	"EmployeeName"	TEXT, "Department" TEXT,
	"DateOfJoining" DATE, "PhotoFileName" TEXT,
 	PRIMARY KEY (EmployeeId)
 );
```
`select * from EmployeeApp_departments;`
`select * from EmployeeApp_employees;`


`INSERT INTO EmployeeApp_departments VALUES (1, 'IT');`

```
INSERT INTO EmployeeApp_employees VALUES (1, 'Bob', 'IT', '2023-04-03', 'https://fastly.picsum.photos/id/959/200/200.jpg?hmac=UDtS3dVizIhIBL6FtIOWaQsq6bJgKWm4f_7SYhWoN9o');
}
```