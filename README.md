# employee-manager
A demonstration of using Python and Django to build a Rest API.

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
