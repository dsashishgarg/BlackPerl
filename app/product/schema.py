from marshmallow import fields, Schema


class ProductSchema(Schema):
    """Product schema"""

    product_id = fields.Number(attribute="product_id")
    product_name = fields.String(attribute="product_name")
    product_price = fields.Float(attribute="product_price")
