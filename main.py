import gym
import gym_chess
import random
import sys
import os

path = os.path.abspath("api")
sys.path.append(path)
from api.stockfish import getMoveReward

# Gym documentation: https://gymnasium.farama.org/api/env/#gymnasium.Env.step
env = gym.make('Chess-v0')
env.reset()

done = False
action = random.choice(list(env.legal_moves))
observation, reward, done, trunc = env.step(action)
reward = getMoveReward(str(observation).split('\n'))
print(reward)
# while not done:
#     action = random.choice(list(env.legal_moves))
#     obs, _, done, trunc = env.step(action)
#     rew = getMoveReward('boardString')
#     print('action', action, 'reward', rew)

env.close()
