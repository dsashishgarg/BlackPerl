from app.product.schema import ProductSchema
from flask_sqlalchemy import SQLAlchemy
from typing import List
from .conftest import app, db
from app.product.models import ProductModel
from app.product.service import ProductService


def test_get_all(db: SQLAlchemy):
    one: ProductModel = ProductModel(product_name="one",
                                     product_price=100)
    two: ProductModel = ProductModel(product_name="two",
                                     product_price=90)
    db.session.add(one)
    db.session.add(two)
    db.session.commit()

    results: List[ProductModel] = ProductModel.query.all()

    assert len(results) == 2
    assert one in results and two in results


def test_delete_by_id(db: SQLAlchemy):
    one: ProductModel = ProductModel(product_name="one",
                                     product_price=100)
    two: ProductModel = ProductModel(product_name="two",
                                     product_price=90)

    db.session.add(one)
    db.session.add(two)
    db.session.commit()

    ProductService.delete_by_id(1)
    db.session.commit()

    results: List[ProductModel] = ProductModel.query.all()

    assert len(results) == 1
    assert one not in results and two in results


def test_create(db: SQLAlchemy):

    one: ProductSchema = dict(
        product_name="new product", product_price=90)
    ProductService.create(one)
    results: List[ProductModel] = ProductModel.query.all()

    assert len(results) == 1

    for k in one.keys():
        assert getattr(results[0], k) == one[k]
