import json

class Chamado:

    ESTADO_ABERTO = 0
    ESTADO_ATENDIMENTO = 1
    ESTADO_FECHADO = 2

    CATEGORIA_CHAMADO_EXTERNO = 'Chamado-Externo' 
    CATEGORIA_CHAMADO_INTERNO = 'Chamado-Interno'
    CATEGORIA_COM_SOCIAL = 'Comunicação-Social'
    CATEGORIA_URGENTE = 'Label-Urgente'
    CATEGORIA_SEM_CATEGORIA = 'Sem-Categoria' 

    def __init__(self, titulo, descricao, categoria, estado = ESTADO_ABERTO):
        self.titulo = titulo
        self.descricao = descricao
        self.estado = estado
        self.categoria = categoria

class TrelloConfig:

    def __init__(self, configAddr = './api_info.json'):
        cfg = None
        with open(configAddr, 'r') as json_file:
             cfg = json.loads(json_file.read())

        self.trelloApiKey = cfg['api_key']
        self.trelloApiSecret = cfg['api_secret']
        self.trelloToken = cfg['token']
        self.trelloTokenSecret = cfg['token_secret']
        self.trelloBoard = cfg['board']
        self.trelloTodoList = cfg['todo']
        self.trelloDoing = cfg['doing']
        self.trelloDoneList = cfg['done']
