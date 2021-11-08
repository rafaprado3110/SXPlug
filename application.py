from flask import Flask, jsonify, request

application = Flask(__name__)

state = {
        "potencia": 0,
        "data": '00/00/0000',
        "hora": '00:00',
        "value": 0
}



@application.route('/', methods =['GET'])
def raiz():
    return "Bem vindo ao SX-Plug"

@application.route('/PegaStatus', methods =['GET'])
def GetState():
    return jsonify(state)

@application.route('/MudaStatus', methods =['POST'])
def ChangeState():
    data = request.get_json()
    state.update(data)

    return jsonify(data)
