from trello import TrelloClient
import json

#Include parent dir on import
import sys
sys.path.insert(0, '..')

from DAO import TrelloChamadoDAO
from Domain import Chamado

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
