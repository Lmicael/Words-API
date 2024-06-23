from flask import request, jsonify, abort
from utils.countVowelsUtil import count_vowels

def vowel_count():
    if not request.is_json:
        abort(400, description="Content-Type must be application/json")
    
    data = request.get_json()
    if "words" not in data or not isinstance(data["words"], list):
        abort(400, description="Request must contain a 'words' list")
    
    result = {word: count_vowels(word) for word in data["words"]}
    return jsonify(result), 200

