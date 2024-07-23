# Reinforcement-Learning-Mario

This is a simple codebase designed for beginners to understand the basics of Reinforcement Learning using GYM.

Many people struggle with incomplete solutions when following online tutorials for this topic. Even though this project uses older versions of libraries, and some people may have moved to another projetcs, I decided to share it in the hope it might help others get started.

**If you find any errors or have the time to update this project, feel free to do so. I would be happy for your contribution!**

I'm posting this because in the early days I was doing this and I was having so much trouble that I left it for some time. Later, with a little more time from my job and more persistence, I made it work, at least until now.

Some people may experience some problemns with the versions of some others tools, so I made a list for that to work.

**Note:** As of today, GYM has been updated to "gymnasium." You can find more information here: https://gymnasium.farama.org/index.html

**Dependencies**

This project relies on specific versions of libraries to ensure compatibility. Here's the complete list for installation:

```bash
pip install nes-py
pip install gym-super-mario-bros==7.3.0
pip install setuptools==65.5.0 "wheel<0.40.0"
pip install gym==0.21.0
pip install stable-baselines3[extra]==1.6.0  # Preferred version

# Alternative for potential issues:
pip install stable-baselines3[extra]==1.3 
