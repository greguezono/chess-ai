import gym
import gym_chess
import random

import sys
import os

path = os.path.abspath("api")
sys.path.append(path)
from api.stockfish import getMoveReward

env = gym.make('Chess-v0')
print(env.render())
env.reset()


done = False
while not done:
    action = random.choice(list(env.legal_moves))
    obs, _, done, trunc = env.step(action)
    rew = getMoveReward('boardString')
    print('')
    print('action', action, 'reward', rew)
    print(env.render(mode='unicode'))

env.close()
