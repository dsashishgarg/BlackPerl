from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import ProductSchema
from .service import ProductService
from .models import ProductModel

from utils.logger import get_logger, api_response_time, LogDetails, ApiStatus, log_details_to_string, ApiName
from datetime import datetime

api = Namespace("Product", description="Product related API's")  # noqa

LOG = get_logger(__name__)


@api.route("/")
class ProductResource(Resource):
    """Products"""

    @responds(schema=ProductSchema, many=True)
    def get(self) -> List[ProductModel]:
        """Get all Products"""
        start = datetime.now()
        log_details = LogDetails.parse_obj({
            'api_name': ApiName.getall,
            'status_code': 'NA',
            'start_time': start,
            'message': 'NA'
        })
        log_details.api_status = ApiStatus.SUCCESS
        api_response_time(log_details)
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
        """Get Single Product"""

        return ProductService.get_by_id(prouduct_id)

    def delete(self, prouduct_id: int) -> Response:
        """Delete Single Product"""
        from flask import jsonify

        id = ProductService.delete_by_id(prouduct_id)
        return jsonify(dict(status="Success", id=id))
