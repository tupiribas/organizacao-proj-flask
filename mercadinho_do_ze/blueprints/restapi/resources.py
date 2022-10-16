from flask import abort, jsonify
from flask_restful import Resource

from mercadinho_do_ze.models import Produtos


class ProductResource(Resource):
    def get(self):
        products = Produtos.query.all() or abort(204)
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )


class ProductItemResource(Resource):
    def get(self, product_id):
        product = Produtos.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.to_dict())
