import mysql.connector
from datetime import datetime
from flask import Flask, jsonify, request

application = Flask(__name__)

state = {
        "value": 0
}

potencia = {
    "Pot": "00"
}

banco = mysql.connector.connect(host="database-2.cgnraaiqytel.us-west-2.rds.amazonaws.com", user="admin", password="usuariopi6", database="infos" )

@application.route('/', methods =['GET'])
def raiz():
    return "Bem vindo ao SX-Plug"

@application.route('/Potencia', methods = ['POST'])
def Potencia2():
    data = request.get_json()
    potencia.update(data)

    now = datetime.today()
    today = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M")
    print(today)
    print(hour)

    bd = banco.cursor()
    bd.execute("INSERT INTO informacoes VALUES ('" + today + "', '" + hour + "', " + potencia["Pot"] + ")")
    banco.commit()
    return ("INSERT INTO informacoes VALUES ('" + today + "', '" + hour + "', " + potencia["Pot"] + ")")

@application.route('/PegaStatus', methods =['GET'])
def GetState():
    return jsonify(state)

@application.route('/MudaStatus', methods =['POST'])
def ChangeState():
    data = request.get_json()
    state.update(data)

    return jsonify(data)
