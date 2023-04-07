from app import db
from app.models.roles_model import RolesModel
from app.schemas.roles_schema import RolesResponseSchema


class RolesController:
    def __init__(self):
        self.model = RolesModel
        self.schema = RolesResponseSchema

    def all(self, query):
        try:
            page = query['page']
            per_page = query['per_page']

            records = self.model.where(status=True).order_by('id').paginate(
                page=page, per_page=per_page
            )
            response = self.schema(many=True)

            return {
                'results': response.dump(records.items),
                'paginate': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }, 200

        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
        
    def getById(self, id):
        try:
            record = self.model.where(id=id).first()
            if record:
                response = self.schema(many=False)

                return {
                    'result': response.dump(record)
                }, 200
            return {
                'message': f'No se encontro rol {id}'
            }, 404

        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
        
    def create(self, data):
        try:
            new_record = self.model.create(**data)
            db.session.add(new_record)
            db.session.commit()

            return {
                'message': f'Se creo rol {data["name"]}, con exito'
            }, 200
        
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
        
    def update(self, id, data):
        try:
            record = self.model.where(id=id).first()
            if record:
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                return {
                    'message': f'Se actualizo rol {id}, con exito'
                }, 201
            return {
                'message': f'No se encontro rol {id}'
            }, 404
        
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
        
    def delete(self, id):
        try:
            record = self.model.where(id=id).first()
            if record and record.status:
                record.update(status=False)
                db.session.add(record)
                db.session.commit()

                return {
                    'message': f'Se deshabilito el rol {id}, con exito'
                }, 201
            return {
                'message': f'No se encontro rol {id}'
            }, 404
        
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500