from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]
# POST - used to receive data, from API perspective
# GET - used to send data back only, from API perspective

# default route
@app.route('/')
def home():
    return render_template('index.html')

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
# 'https://127.0.0.1:5000/store/some_name'
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
        return jsonify({'message': 'store NOT found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()            
    for store in stores:
        if store["name"] == name:
            new_item = {
                'items': request_data['name'],
                'price': request_data['price']                
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store NOT found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store NOT found'})

app.run(port=5000)