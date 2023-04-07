from app import api
from flask_restx import Resource


role_ns = api.namespace(
    name='Roles',
    description='Rutas de roles',
    path='/roles'
)


@role_ns.route('')
class Roles(Resource):
    def get(self):
        ''' Listar todos los roles '''
        pass

    def post(self):
        ''' Creacion de roles '''
        pass

@role_ns.route('/<int:id>')
class RolesId(Resource):
    def get(self, id):
        ''' Traer rol por ID '''
        pass

    def put(self, id):
        ''' Actualizar rol por ID '''
        pass

    def delete(self, id):
        ''' Deshabilitar rol por ID '''
        pass