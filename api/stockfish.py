import requests
import io
import json

URL = "https://stockfish.online/api/stockfish.php?"
# fen = 'r2q1rk1/ppp2ppp/3bbn2/3p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 11'
DEPTH = '5'
MODE = 'eval'

def getMoveReward(board):
    fen = boardToFen(board)
    endpoint = URL + 'fen=' + fen + '&depth=' + DEPTH + '&mode=' + MODE
    response = requests.get(endpoint)
    reward = getRewardFromResponse(response)
    return reward

def boardToFen(board):
    # Use StringIO to build string more efficiently than concatenating
    with io.StringIO() as s:
        for row in board:
            empty = 0
            for c in row:
                if c.isalpha():
                    if empty > 0:
                        s.write(str(empty))
                        empty = 0
                    s.write(c)
                elif (c == '.'):
                    empty += 1
            if empty > 0:
                s.write(str(empty))
            s.write('/')
        # Move one position back to overwrite last '/'
        s.seek(s.tell() - 1)
        # If you do not have the additional information choose what to put
        s.write(' w KQkq - 0 1')
        return s.getvalue()

def getRewardFromResponse(response):
    responseMap = json.loads(response.text)
    rawText = responseMap['data']
    reward = ''
    for i in range(len(rawText)):
        if (rawText[i] == '-' or rawText[i] == '.' or rawText[i].isnumeric()):
            reward += rawText[i]
    return float(reward)
