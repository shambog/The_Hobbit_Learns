# The_Hobbit_Learns
## Reinforcement learning using the Q-learning approach of rewards.


The Hobbit is excited to begin his treasure hunt after seeing Thror's map. The journey is full of obstacles but the Hobbit learns from his mistakes and finally finds the treasure overcoming all the obstacles that came along the way.

In this project, we are implementing the Q-Learning algorithm. It is a model-free reinforcement learning algorithm where the goal is to learn a policy which tells our Hobbit what action to take in which situatuon. The algorithm does not require a model of the environment and can learn from rewards.


## The Thror's Map

![Treasure_Hunt_In_Progress](https://user-images.githubusercontent.com/35944630/57576577-53813000-7428-11e9-9973-9e3a1da330ed.png)


In this diagram, the RED object is our Hobbit, the ORANGE ones are the obstacles and the GREEN circle is our treasure.

## The Treasure Hunt

In this journey, there are "50" attempts made by Hobbit. In each of those attempts the Hobbit either ends up getting the treasure (rewards = +1), reaches an obstacle (rewards = -1) or stays in the ground state (rewards = 0).

## Installation

Clone the repository and run the Start_Hunting.py file

## Project Files

1. **Map_Environment.py** - Creates the environment for trasure hunt with all the obstacles and the trasure.
2. **Learning_Engine.py** - Has the reinforcement learning logic.
3. **Start_Hunting.py** - Entry to the adventure.
