from app.product.schema import ProductSchema
from .db import db


class ProductModel(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80))
    product_price = db.Column(db.Float(precision=2))

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def json(self):
        return {'product_name': self.product_name, 'product_price': self.product_price}

    @classmethod
    def find_by_id(cls, product_id):
        return cls.query.filter_by(product_id=product_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
