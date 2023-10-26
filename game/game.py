import gym
import gym_chess
import random

env = gym.make('Chess-v0')
print(env.render())

env.reset()
done = False

white = 0
black = 0

isWhite = False
while not done:
    action = random.choice(list(env.legal_moves))
    obs, rew, done, trunc = env.step(action)
    print('')
    print('action', action, 'reward', rew)
    print(env.render(mode='unicode'))

env.close()
