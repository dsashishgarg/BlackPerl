from flask.json import jsonify
from app.product.schema import ProductSchema
from marshmallow.fields import String
from app.product import db
from typing import List
from .models import ProductModel

from flask_restplus import Resource, reqparse


class ProductService:

    @staticmethod
    def create(new_product: ProductSchema) -> ProductModel:
        nproduct = ProductModel(
            product_name=new_product["product_name"], product_price=new_product["product_price"])
        nproduct.save_to_db()
        return nproduct

    @staticmethod
    def get_all() -> List[ProductModel]:
        return ProductModel.query.all()

    @staticmethod
    def get_by_id(product_id: int) -> ProductModel:
        return ProductModel.find_by_id(product_id)

    @staticmethod
    def delete_by_id(product_id: int) -> List[int]:
        product = ProductModel.query.filter(
            ProductModel.product_id == product_id).first()
        if not product:
            return []
        product.delete_from_db()
        return [product_id]
