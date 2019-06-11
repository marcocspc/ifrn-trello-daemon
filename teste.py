from trello import TrelloClient
import json

auth = None

with open('./api_info.json', 'r') as json_file:
    auth = json.loads(json_file.read())

client = TrelloClient(
    api_key=auth['api_key'],
    api_secret=auth['api_secret'],
    token=auth['token'],
    token_secret=auth['token_secret']
)

all_boards = client.list_boards()
print(all_boards)
test_board = all_boards[1]
print(test_board.list_lists())
lists = test_board.all_lists() #[<List To Do>, <List Doing>, <List Done>] 
my_list = test_board.get_list(lists[0].id)

for card in my_list.list_cards():
    print(card.name)
