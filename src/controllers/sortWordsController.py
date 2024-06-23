from flask import request, jsonify, abort

def sort_words():
    if not request.is_json:
        abort(400, description="Content-Type must be application/json")
    
    data = request.get_json()
    if "words" not in data or not isinstance(data["words"], list):
        abort(400, description="Request must contain a 'words' list")
    
    if "order" not in data:
        abort(400, description="Request must contain an 'order' parameter")
    
    order = data["order"]
    if order not in ["asc", "desc"]:
        abort(400, description="Order must be 'asc' or 'desc'")
    
    sorted_words = sorted(data["words"], reverse=(order == "desc"))
    return jsonify(sorted_words), 200
