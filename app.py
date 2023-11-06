from flask import Flask, jsonify, request

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['ENV'] = 'development'


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE']) # GET by Default
def main():
    
    data = {
        "message": "Server Up"
    }
    
    return jsonify(data), 200

# enviar datos en la url como parametros
@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    
    return jsonify({ "id": id }), 200

# enviar datos en la url como query string
@app.route('/user', methods=['GET'])
def get_user_by_query_string():
    
    query = request.args
    name = query['name']
    pt = query['pt']
    
    
    return jsonify({ "name": name, "pt": pt }), 200

@app.route('/user', methods=['POST'])
def enviar_datos_de_usuario():
    
    # Capturamos todo el body en un diccionario
    body = request.get_json()
    
    if not 'name' in body:
        return jsonify({ "msg": "Name is required!"}), 400
    
    # Capturamos los datos de manera individual
    name = request.json.get("name")
    lastname = request.json.get("lastname")
    
    return jsonify({ "body": body, "name": name, "lastname": lastname })

@app.route('/user', methods=['PUT'])
def actualizar_datos_de_usuario():
    
    if not 'username' in request.form:
        return jsonify({"msg": "username is required!"}), 422
    
    # Enviando datos mediante un formulario con archivo adjunto
    username = request.form["username"]
    password = request.form["password"]
    
    # Recibiendo un archivo adjunto
    avatar = request.files["avatar"]
    
    return jsonify({ "username": username, "password": password, "avatar": avatar.filename }), 200


@app.route('/noticias', methods=['GET', 'POST']) # buscar todas las noticias o crear una nueva noticia
@app.route('/noticias/<int:id>', methods=['GET', 'PUT', 'DELETE']) # Buscar una noticia por id, actualizar una noticia por id o eliminar una noticia por id
def noticias(id = None):
    
    if request.method == 'GET':
        
        if id is not None:
            return jsonify({ "message": "Buscando con id "}), 200
        else:
            return jsonify({ "message": "Buscando todas las noticias "}), 200
            
    if request.method == 'POST':
        return jsonify({ "message": "creando una noticia"}), 200
            
    if request.method == 'PUT':
        return jsonify({ "message": "actualizando una noticia"}), 200
    
    if request.method == 'DELETE':
        return jsonify({ "message": "eliminando una noticia"}), 200


if __name__ == '__main__':
    app.run()