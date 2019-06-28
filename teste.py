from trello import TrelloClient
import json
from DAO import TrelloChamadoDAO
from Domain import Chamado

#auth = None
#
#with open('./api_info.json', 'r') as json_file:
#    auth = json.loads(json_file.read())
#
#client = TrelloClient(
#    api_key=auth['api_key'],
#    api_secret=auth['api_secret'],
#    token=auth['token'],
#    token_secret=auth['token_secret']
#)
#
#all_boards = client.list_boards()
#print(all_boards)
#test_board = all_boards[1]
#print(test_board.list_lists())
#lists = test_board.all_lists() #[<List To Do>, <List Doing>, <List Done>] 
#my_list = test_board.get_list(lists[0].id)
#
#for card in my_list.list_cards():
#    print(card.name)

tcd = TrelloChamadoDAO()

chamados = tcd.selectAllDoneChamados()

res = {
    Chamado.CATEGORIA_CHAMADO_EXTERNO: 0,
    Chamado.CATEGORIA_CHAMADO_INTERNO: 0,
    Chamado.CATEGORIA_COM_SOCIAL: 0,
    Chamado.CATEGORIA_URGENTE: 0,
    Chamado.CATEGORIA_SEM_CATEGORIA: 0
}

for chamado in chamados:
    if chamado.categoria == Chamado.CATEGORIA_CHAMADO_EXTERNO:
        res[Chamado.CATEGORIA_CHAMADO_EXTERNO] += 1
    elif chamado.categoria == Chamado.CATEGORIA_CHAMADO_INTERNO:
        res[Chamado.CATEGORIA_CHAMADO_INTERNO] += 1
    elif chamado.categoria == Chamado.CATEGORIA_COM_SOCIAL:
        res[Chamado.CATEGORIA_COM_SOCIAL] += 1
    elif chamado.categoria == Chamado.CATEGORIA_URGENTE:
        res[Chamado.CATEGORIA_URGENTE] += 1
    elif chamado.categoria == Chamado.CATEGORIA_SEM_CATEGORIA:
        res[Chamado.CATEGORIA_SEM_CATEGORIA] += 1

print(res)
