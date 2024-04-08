# Triduum_test

## Table of Contents
- [Triduum\_test](#triduum_test)
  - [Table of Contents](#table-of-contents)
  - [General Info](#general-info)
  - [Technologies](#technologies)
  - [Installation](#installation)
  - [SQL](#sql)
***

## General Info
Ecommerce API built in Django rest framework using Python.  Project was developed by Kevin Andres Blandon Velez.

## Technologies
***
A list of technologies used within the project:
* [Django](https://www.djangoproject.com/): Version 4.1.7
* [Djangorestframework](https://www.django-rest-framework.org/): Version 3.14.0
* [Python](https://www.python.org/): Version 3.11

## Installation
***
About the installation:

Use pip
You can install the project by running this command:
```
py -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
py .\manage.py makemigrations
py .\manage.py migrate
py .\manage.py runserver
```

## SQL
***
Sql scripts to perform the queries can be found at the following location:

ecommerceapi\Scripts

Question: QUEREMOS SABER DE LAS ORDENES, CUANTAS TIENEN EL PRODUCTO 2.

The solution to the question is in the file ecommerceapi\Scripts\consulta_ordenes_cantidad.sql

And Question: se requiere la creación de una consulta SQL que permita saber cual es el producto que más ha sido ordenado y en qué
cantidades (se requiere mínimo la creación de 2 órdenes con el mismo producto para
realizar esta consulta).
The solution to the question is in the file ecommerceapi\Scripts\consulta_producto_mas_ordenado_y_cantidades.sql
