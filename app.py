from flask import Flask, request
from helpers import listaMembros, listaMembro, adicionaMembro

app = Flask(__name__)

@app.route('/listar-membros')
def listar_membros():
    membros = listaMembros()
    return membros

@app.route('/lista-membro/<int:id>')
def lista_membro(id):
    membro = listaMembro(id)
    return membro

@app.route('/adicionar-membro', methods=['POST'])
def adiciona_membro():
    data_json = request.get_json()
    resp = adicionaMembro(data_json)
    return resp

if __name__ == '__main__':
    app.run()
    