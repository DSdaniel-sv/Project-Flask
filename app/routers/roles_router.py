from app import api
from flask import request
from flask_restx import Resource
from app.schemas.roles_schema import RolesRequestSchema
from app.controllers.roles_controller import RolesController


role_ns = api.namespace(
    name='Roles',
    description='Rutas de roles',
    path='/roles'
)

schema = RolesRequestSchema(role_ns)

@role_ns.route('')
class Roles(Resource):
    @role_ns.expect(schema.all(), validate=True)
    def get(self):
        ''' Listar todos los roles '''
        query = schema.all().parse_args()
        controller = RolesController()
        return controller.all(query)
    
    @role_ns.expect(schema.create(), validate=True)
    def post(self):
        ''' Creacion de roles '''
        controller = RolesController()
        return controller.create(request.json)

@role_ns.route('/<int:id>')
class RolesId(Resource):
    def get(self, id):
        ''' Traer rol por ID '''
        controller = RolesController()
        return controller.getById(id)

    @role_ns.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar rol por ID '''
        controller = RolesController()
        return controller.update(id, request.json)

    def delete(self, id):
        ''' Deshabilitar rol por ID '''
        controller = RolesController()
        return controller.delete(id)