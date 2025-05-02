# CONSUMO DE ENDPOINT */usuarios/listar* con GraphQL 

## SET UP
En la configuración del microservicio de GraphQL, se modificaron los siguientes parámetros:

## DEPENDENCIAS
Para que el proyecto funcione correctamente, más espcíficamente referido al consumo del
endpoint con GraphQL, se debe instalar las siguientes dependencias:

> pip install django django-cors-headers graphene graphene-django requests psycopg2-binary supabase

## Django Application
Para lograr que GraphQL consuma exitosamente los datos del endpoint, se necesita crear una aplicación de
django contenida que sirva como la base del microservicio, utilizando un esquema *schema.py* para la 
obtención de los datos, creando esta aplicación con el siguiente comando:

> python manage.py startapp graphql_service

## Direccionamiento para GraphQL
Primeramente, en el archivo *urls.py* del directorio original, se añadió el siguiente *path*:

urlpatterns = [
   ...
   path('microservice/graphql/', GraphQLView.as_view(graphiql=True)),
]

Después, en el archivo *urls.py* de la aplicación Django, se añadió lo siguiente:

from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]


Luego, en el archivo *settings.py* del directorio original, se añadió lo siguiente:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'graphene_django',
    'graphql_service',
]

GRAPHENE = {
    "SCHEMA": "graphql_service.schema.schema"
}

## Esquema para el Query
En la aplicación de Django **graphql_service**, se añadió el archivo *schema.py* con las especificaciones
de los tipos de datos del usuario (ID, String, etc) y se añadió una clase para el *Query* para GraphQL para
poder obtener los datos del listado de usuarios

## Query en la interfaz de GraphQL
Finalmente, se levantó el servidor para el proyecto:
> python manage.py runserver

Y se ubicó en la dirección:
> http://127.0.0.1:8000/microservice/graphql 

lo cual nos permite ejecutar el siguiente *query*:
query {
  usuarios {
    idusuario
    usuario
    correo
    rol
  }
}

Esto finalmente devuelve los datos del endpoint */usuarios/listar*