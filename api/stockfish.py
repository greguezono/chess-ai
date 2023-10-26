import requests

URL = "https://stockfish.online/api/stockfish.php?"
# fen = 'r2q1rk1/ppp2ppp/3bbn2/3p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 11'
DEPTH = '5'
MODE = 'eval'

def getMoveReward(boardString):
    endpoint = URL + 'fen=' + boardString + '&depth=' + DEPTH + '&mode=' + MODE
    response = requests.get(endpoint)
    print(response.text)
    return 1
