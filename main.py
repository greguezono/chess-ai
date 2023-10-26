import gym
import gym_chess
import random

import sys
import os

path = os.path.abspath("api")
sys.path.append(path)
from api.stockfish import getBestMove

env = gym.make('Chess-v0')
print(env.render())
env.reset()


done = False
# while not done:
#     action = random.choice(list(env.legal_moves))
#     obs, rew, done, trunc = env.step(action)
#     print('')
#     print('action', action, 'reward', rew)
#     print(env.render(mode='unicode'))

getBestMove()
env.close()
