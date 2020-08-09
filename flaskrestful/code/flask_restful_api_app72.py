from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates new end point /auth
items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        # could use list instead of next if more than one item in list.
        item = next(filter(lambda x: x['name'] == name, items), None)
        # ternary operator.
        # return {'item': item}, 200 if item is not None else 404
        # shortened to
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # arguments handy are force=True, but can be dangerous, or silent=True
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        data = request.get_json()

        if (item):
            item['price'] = data['price']
        else:
            item = {'name': name, 'price': data['price']}
            items.append(item)
            
        return item, 201
        

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# port 5000 is default so argument not really necessary.
app.run(port=5000, debug=True)