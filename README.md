# Employee Manager API
A demonstration of using Python and Django to create a Rest API.

This app implements a hypothetical scenario of an HTTP REST API that lets you list, retrieve, create, update, and delete employees and departments from an employee management system.

An administration panel is also available for data maintenance.
### Deploy
The application was deployed in Heroko and can be accessed through these links: [Api Root](https://llab-employee-dev.herokuapp.com/api/). [Api Admin](https://llab-employee-dev.herokuapp.com/admin/). (*login: admin, password: adminadmin*)

To serve the static files the AWS S3 service is being used.

The database used is Postgres.

### API Documentation
An API documentation can be found [here](https://documenter.getpostman.com/view/3590276/SVfMSq5c).


# The problem
Our team is growing every month and now we need to have some application to manage employees' information, such as name, e-mail and department. The application must have an API to allow integrations.

# Deliverables
The app must have:
- A Django Admin panel to manage employees' data
- An API to list, add and remove employees

# API example (list)
**Request**

`curl -H "Content-Type: application/javascript" http://localhost:8000/employee/`

**Response**

```
[
  {
    "name": "Arnaldo Pereira",
    "email": "arnaldo@teste.com",
    "department": "Architecture"
  },
  {
    "name": "Renato Pedigoni",
    "email": "renato@teste.com",
    "department": "E-commerce"
  },
  {
    "name": "Thiago Catoto"",
    "email": "cototo@teste.com",
    "department": "Mobile"
  }
]
```
# Installing and testing instructions
1. Clone the repository;  
2. Create a virtual environment;
3. Activate the virtual environment;
4. Install the dependencies;
5. Configure the instance with .env;
6. Run data migration;
7. Run the tests;
8. Create super user;
9. Run Django Server.

```console
git clone https://github.com/alcfernandes/employee-manager.git
cd employee-manager/
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py migrate
python manage.py test
python manage.py createsuperuser
python manage.py runserver
```
