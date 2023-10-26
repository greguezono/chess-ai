import requests

url = "https://stockfish.online/api/stockfish.php?"

fen = 'r2q1rk1/ppp2ppp/3bbn2/3p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 11'
depth = '5'
mode = 'eval'

endpoint = url + 'fen=' + fen + '&depth=' + depth + '&mode=' + mode

response = requests.get(endpoint)
print(response.text)

def getBestMove():
    print('hi')
