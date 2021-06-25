from dynamorm import DynaModel
from marshmallow import fields
from django.conf import settings

class Kitchen(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoint_url' : settings.DB_ENDPOINT
        }
        name = settings.DB_TABLE
        hash_key = 'model_name'
        read = 25
        write = 5
    
    class Schema:
        model_name = fields.String()
        name = fields.String()
        data = fields.String()
        id = fields.Integer()