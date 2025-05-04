import json
from graphene.test import Client
from graphql_service.schema import schema
import requests_mock

def test_usuarios_query():
    mock_response = {
        "usuarios": [
            {
                "idusuario": 1,
                "usuario": "test_user",
                "correo": "test@example.com",
                "rol": "Tester"
            }
        ]
    }
    
    with requests_mock.Mocker() as m:
        m.get('http://127.0.0.1:8000/usuarios/listar/', 
              json=mock_response)
        
        client = Client(schema)
        query = '''
            query {
                usuarios {
                    idusuario
                    usuario
                    correo
                    rol
                }
            }
        '''
        result = client.execute(query)
        
        assert 'errors' not in result
        assert result['data']['usuarios'][0]['usuario'] == 'test_user'
        assert len(result['data']['usuarios']) == 1

def test_create_user_mutation():
    from graphql_service.schema import schema
    print("Mutaciones disponibles:", schema.introspect()['__schema']['mutationType'])
    
    client = Client(schema)
    mutation = '''
        mutation {
            createUser(username: "new", email: "new@test.com") {
                user {
                    idusuario
                    usuario
                }
            }
        }
    '''
    result = client.execute(mutation)
    print("Resultado completo:", result)
    
    assert 'errors' not in result, f"GraphQL errors: {result['errors']}"
    assert result['data']['createUser']['user']['usuario'] == 'new'
    client = Client(schema)
    mutation = '''
        mutation {
            createUser(username: "new", email: "new@test.com") {
                user {
                    idusuario
                    usuario
                }
            }
        }
    '''
    result = client.execute(mutation)
    
    print("Resultado mutacion:", result)
    
    assert result.get('data') is not None, "No data in response"
    assert result['data']['createUser']['user']['usuario'] == 'new'
    assert result['data']['createUser']['user']['idusuario'] == '999'