import json

def listaMembros():
    with open('membros.json', encoding='utf-8') as arquivo:
        return json.load(arquivo) 
    
def listaMembro(id):
    todos_membros = listaMembros()

    for membro in todos_membros['membros']:
        if membro['id'] == id:
            return membro
        
def proximoId():
    membros = listaMembros()
    tamanho_membros = len(membros['membros'])
    return tamanho_membros+1

def adicionaMembro(data_json):
    
    try:
        carrega_todos_membros = listaMembros()
        todos_membros = carrega_todos_membros['membros']
        membro_novo = data_json
        id = proximoId()
        membro_novo['id'] = id
        todos_membros.append(membro_novo)
        
        with open('membros.json', 'w', encoding='utf-8') as arquivo:
            json.dump(todos_membros, arquivo, indent=4)
        return {"status": True}
    except Exception as E:
        return {"status": False, "erro": E}
    
def listaProjetos():
    with open('projetos.json', encoding='utf-8') as arquivo:
        return json.load(arquivo) 