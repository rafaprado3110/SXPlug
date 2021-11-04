from flask import Flask, jsonify, request

application = Flask(__name__)
app = application

state = { "value" : 1} 

@application.route('/', methods =['GET'])
def home():
    return "Seja Bem Vindo ao VNCS-13"

@application.route('/GetState', methods =['GET'])
def GetState():
    return jsonify(state)

@application.route('/AppChangeState', methods =['GET'])
def AppChangeState():
    if state['value'] == 1:
        state['value'] = 0
    else:
        state['value'] = 1

    return jsonify(state)

@application.route('/NodeChangeState', methods =['POST'])
def NodeChangeState():
    data = request.get_json()
    state.update(data)

    return jsonify(data)
