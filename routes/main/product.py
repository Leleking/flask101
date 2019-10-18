from flask import Blueprint, jsonify, request
from models.products import Products, product_schema, products_schema, db
product = Blueprint('product', __name__)

# save product
@product.route('/products', methods=['POST'])
def store():
   name = request.json['name']
   description = request.json['description']
   price = request.json['price']
   qty = request.json['qty']

   product = Products(name, description, price, qty)
   
   db.session.add(product)
   db.session.commit()

   return product_schema.jsonify(product)

# Get all products
@product.route('/products', methods=['GET'])
def index():
    products  = Products.query.all()
    products = products_schema.dump(products)
    return jsonify(products)


# Get a product
@product.route('/products/<id>',methods=['GET'])
def show(id):
    product = Products.query.get(id)
    return product_schema.jsonify(product)


@product.route('/products/1', methods=['PUT'])
def update(id):
    product = Products.query.get(id)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty
    db.session.commit()

    return product_schema.jsonify(product)
