from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import ProductSchema
from .service import ProductService
from .models import ProductModel

api = Namespace("Product", description="Product related API's")  # noqa


@api.route("/")
class ProductResource(Resource):
    """Products"""

    @responds(schema=ProductSchema, many=True)
    def get(self) -> List[ProductModel]:
        """Get all Products"""

        return ProductService.get_all()

    @accepts(schema=ProductSchema, api=api)
    @responds(schema=ProductSchema)
    def post(self) -> ProductModel:
        """Create a Single Product"""

        return ProductService.create(request.parsed_obj)


@api.route("/<int:prouduct_id>")
@api.param("prouduct_id", "Product database ID")
class ProducttIdResource(Resource):
    @responds(schema=ProductSchema)
    def get(self, prouduct_id: int) -> ProductModel:
        """Get Single Widget"""

        return ProductService.get_by_id(prouduct_id)

    def delete(self, prouduct_id: int) -> Response:
        """Delete Single Product"""
        from flask import jsonify

        id = ProductService.delete_by_id(prouduct_id)
        return jsonify(dict(status="Success", id=id))
