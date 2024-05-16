from flask import request, jsonify, current_app as app

counter = 0

@app.route('/greeting', methods=['GET'])
def greeting():
    global counter
    name = request.args.get('name', 'World')
    counter += 1
    return jsonify({'id': counter, 'content': f'Hello, {name}!'})
