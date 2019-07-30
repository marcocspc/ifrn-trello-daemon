from Domain import TrelloConfig 
from trello import TrelloClient

class ConnectionSingleton:
   
    TRELLO_CONN = None

    def getTrelloConnection(self):
        if ConnectionSingleton.TRELLO_CONN == None:
            self.cfg = TrelloConfig()

            client = TrelloClient(
                api_key = self.cfg.trelloApiKey,
                api_secret = self.cfg.trelloApiSecret,
                token = self.cfg.trelloToken,
                token_secret = self.cfg.trelloTokenSecret
            ) 

            ConnectionSingleton.TRELLO_CONN = client

            return ConnectionSingleton.TRELLO_CONN
        else:
            return ConnectionSingleton.TRELLO_CONN
