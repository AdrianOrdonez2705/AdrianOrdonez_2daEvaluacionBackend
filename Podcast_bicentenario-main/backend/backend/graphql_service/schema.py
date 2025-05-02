import graphene
import requests

class UserType(graphene.ObjectType):
    idusuario = graphene.ID()
    usuario = graphene.String()
    correo = graphene.String()
    fecha_ingreso = graphene.String()
    rol = graphene.String()

class Query(graphene.ObjectType):
    usuarios = graphene.List(UserType)

    def resolve_usuarios(self, info):
        response = requests.get("http://127.0.0.1:8000/usuarios/listar/")
        if response.status_code == 200:
            data = response.json()
            return data.get('usuarios', [])
        return []

schema = graphene.Schema(query=Query)