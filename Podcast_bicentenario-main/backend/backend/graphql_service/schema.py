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
    

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, username, email):
        return CreateUser(user={
            "idusuario": 999, 
            "usuario": username,
            "correo": email,
            "rol": "Test"
        })

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)