from flask import Flask ,  jsonify , request

app = Flask(__name__)

items = [
    { 
        'id': 1 , 
        'name' : "Item name" , 
        "description" : "Item Description"
    },
    {
        'id': 2 , 
        'name' : "Item name" , 
        "description" : "Item Description"
    }
]
@app.route('/')
def home():
    return "Welcome to Home page"

@app.route('/items' , methods=["GET"])
def get_items():
    return jsonify(items)

@app.route('/items' , methods=['POST'])
def add_item():
    if not request.json or not "name" in request.json:
        return jsonify({"error" : "Error in adding items"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/items/<int:item_id>' , methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error" : "Error in adding items"})
    item['name'] = request.json.get('name' , item['name'])
    item['description'] = request.json.get('description' , item['description'])
    return jsonify(item)


@app.route('/items/<int:item_id>' , methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify(items)




if __name__ == "__main__":
    app.run(debug=True)