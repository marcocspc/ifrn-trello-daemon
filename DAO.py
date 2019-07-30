from Singleton import ConnectionSingleton
from Domain import Chamado

class TrelloChamadoDAO:

    def selectAllDoneChamados(self):
        #Instanciar pytrello
        cns = ConnectionSingleton()
        client = cns.getTrelloConnection()

        #Obter todos os chamados
        all_boards = client.list_boards()
        done_board = all_boards[int(cns.cfg.trelloBoard)]
        lists = done_board.all_lists() #
        my_list = done_board.get_list(lists[int(cns.cfg.trelloDoneList)].id)

        #Converter chamado do pytrello para chamado do domínio
        chamados = []

        for card in my_list.list_cards():
            titulo = card.name

            descricao = card.desc
           
            if card.labels != None:
                cat = str(card.labels[0])[1:-1] 
                cat = cat.split(' ')
                cat = cat[len(cat) - 2] + '-' +  cat[len(cat) - 1]
            else:
                cat = Chamado.CATEGORIA_SEM_CATEGORIA 

            estado = Chamado.ESTADO_FECHADO

            c = Chamado(titulo, descricao, cat, estado)
            chamados.append(c)

        #Retornar os chamados
        return chamados
