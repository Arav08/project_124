from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    { 'id': 1, 'contact': u'9987644456', 'name': u'Raju', 'done': False}, 
    { 'id': 2, 'contact': u'9876543222', 'name': u'Rahul', 'done': False}
]

@app.route('/add-data', methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'please provide the data'
        }, 400)

    contact = {'id': contacts[-1]['id'] + 1, 'name': request.json['name'], 'contact': request.json.get['contact', ""], 'done': False}
    contacts.append(contact)

    return jsonify({'status': 'success', 'message': 'tassk added successfully'})

@app.route('/get-data')
def get_task():
    return jsonify({'data': contacts})

if __name__ == '__main__':
    app.run(debug = True)