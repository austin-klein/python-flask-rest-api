from flask import request, jsonify
from app import app
from model import  db, Product, product_schema, products_schema

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    
    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()
    
    return product_schema.jsonify(new_product)

@app.route('/product', methods=['GET'])
def get_all_products():
 all_products = Product.query.all()
 result = products_schema.dump(all_products)
 return jsonify(result)

@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    
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


@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)