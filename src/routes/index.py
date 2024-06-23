from flask import jsonify
from controllers.vowelCountController import vowel_count
from controllers.sortWordsController import sort_words

def init_routes(app):
    # Rota para contar vogais
    @app.route('/vowel_count', methods=['POST'])
    def post_vowelCount():
        return vowel_count()

    # Rota para ordenar palavras
    @app.route('/sort', methods=['POST'])
    def post_sortWords():
        return sort_words()

    # Rota para tratar rotas inexistentes
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404

    # Rota para tratar métodos não permitidos
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"error": "Method not allowed"}), 405

    # Rota para tratar erros de requisição
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": error.description}), 400
