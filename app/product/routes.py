from .models import ProductModel
from .schema import ProductSchema

BASE_ROUTE = "product"


def register_routes(api, app, root="api"):
    from .controller import api as product_api

    api.add_namespace(product_api, path=f"/{root}/{BASE_ROUTE}")
