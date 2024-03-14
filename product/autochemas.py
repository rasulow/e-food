from drf_yasg.inspectors import SwaggerAutoSchema

class ProductAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        return ['Your App']