#playing mario with python
#nes-py joy pd
#open ai gym

#importing for testing the game
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

#imports for the environment:
from gym.wrappers import GrayScaleObservation
#import for the Vectorization Wrappers
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
#Matplotlib to show the impact of frame stacking
from matplotlib import pyplot as plt
#imports for the train: 
import os #for file path management
from stable_baselines3 import PPO #for algos
from stable_baselines3.common.callbacks import BaseCallback # for saving models
import sys

#the game
#env = gym_super_mario_bros.make('SuperMarioBros-v0')
#env = JoypadSpace (env, SIMPLE_MOVEMENT)
#print(env.observation_space.shape)
#print(SIMPLE_MOVEMENT)

#condition to restart or not
# done = True
# # Loop through each frame in the game
# for step in range(100000):#steps
#     if done:
#         #start the game
#         env.reset()
#         # take randon actions
#     state, reward, done, info = env.step(env.action_space.sample()) #sample allows randon
#     env.render() #show the game on the screen
# env.close() #close the game

## PRE-PROCESSING THE ENVIROMENT FOR THE IA TO LEARN WITH DATA ABOUT THE GAME
# 1. Creating the base environment
env = gym_super_mario_bros.make('SuperMarioBros-v0')
# 2. Simplifying the controls
env = JoypadSpace (env, SIMPLE_MOVEMENT)
# 3. Grayscale
env = GrayScaleObservation(env, keep_dim=True) #this helps to avoid using too much chanels 
# what makes the IA process too much pixel. The shape whithout grayscale is 240*256*3 = 184320
# with the grayscale is 240*256*1 = 61440.   
# 4. Wrap inside the Dummy Environment
env = DummyVecEnv([lambda: env])
# 5. Stack the frames
env = VecFrameStack (env, 4, channels_order='last')
state = env.reset()
#state.shape
state, reward, done, info = env.step([1])
# #using matplotlib to show the frame
# plt.figure(figsize=(20,16))
# for idx in range (state.shape[3]):
#     plt.subplot(1,4,idx+1)
#     plt.imshow(state[0][:,:,idx])
# plt.show()

#3.Training the RL model - Bulding the model:

# class TrainAndLogginCallback(BaseCallback):

#     def __init__(self, check_freq, save_path, verbose = 1):
#         super(TrainAndLogginCallback, self).__init__(verbose)
#         self.check_freq = check_freq
#         self.save_path = save_path
    
#     def _init_callback(self):
#         if self.save_path is not None:
#             os.makedirs(self.save_path, exist_ok=True)
    
#     def _on_step(self):
#         if self.n_calls % self.check_freq == 0:
#             model_path = os.path.join(self.save_path, 'best_model_{}'.format(self.n_calls))
#             self.model.save(model_path)
        
#         return True

# CHECKPOINT_DIR = "F:/Mario Train/train"
# LOG_DIR = "F:/Mario Train/logs"

# # Setup of the model saving callback

# callback = TrainAndLogginCallback(check_freq=10000, save_path=CHECKPOINT_DIR)

# #creating the PPO model

# model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=LOG_DIR, learning_rate=0.000001, n_steps=512)
# #by using the CNN Policy we can train images better, there is the MLP thats great for tabular data

# # train the AI model, where it starts to learn
# model.learn(total_timesteps=1000000, callback=callback)


#4. Running the model live
#load the model

model = PPO.load("F:/Mario Train/train/best_model_1000000.zip")
state = env.reset()
#start the game
state = env.reset()
#loop through the game

while True:

    action, _ = model.predict(state)
    state, reward, done, info = env.step(action)
    env.render()