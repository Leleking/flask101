from config import db, ma


class Products(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(191))
    description = db.Column(db.Text(191), nullable=True)
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product Schema


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
