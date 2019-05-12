# The_Hobbit_Learns
## Reinforcement learning using the Q-learning approach of rewards.

The Hobbit is excited to begin his treasure hunt after seeing Thror's map. The journey is full of obstacles but the Hobbit learns from his mistakes and finally finds the treasure overcoming all the obstacles that came along the way.

In this project, we are implementing the Q-Learning algorithm. It is a model-free reinforcement learning algorithm where the goal is to learn a policy which tells our Hobbit what action to take in which situation. The algorithm does not require a model of the environment and can learn from rewards.

## Authors
* Shambo Ghosh
* Sandip Dey

## The Thror's Map

![Treasure_Hunt_In_Progress](https://user-images.githubusercontent.com/35944630/57576577-53813000-7428-11e9-9973-9e3a1da330ed.png)


In this diagram (our map like environment), the RED object is our Hobbit, the ORANGE ones are the obstacles and the GREEN circle is our treasure.

## The Treasure Hunt Using Q-Learning 

In this journey, there are "50" attempts made by Hobbit. 

In each of those attempts the Hobbit;

* ends up getting the treasure (rewards = +1), 
* reaches an obstacle (rewards = -1) 
* moves around and stays in the ground state (rewards = 0). 

The goal is to find the *optimum* path to the treasure by avoiding all the obstacles.

## Reinforcement Learning

Some of the actions the Hobbit can take are;

* Go UP
* Go DOWN
* Move LEFT
* Move RIGHT

The learning process has the following methods; 

* *Selects* an action
* *Learns* from the actions, considers the 
  * present state
  * the action it takes
  * the rewards it gets 
  * the new state it reaches
* *Checks* if state exists 


Some of the parameters of Q-Learning;

* Learning Rate = 0.01 
* Reward Decay = 0.9 

## Installation

Clone the repository and run the **Start_Hunting.py** file

## Project Structure

1. **Map_Environment.py** - Creates the environment for treasure hunt with all the obstacles and the trasure.
2. **Learning_Engine.py** - Has the reinforcement learning logic.
3. **Start_Hunting.py** - Entry to the adventure.

## References

https://en.wikipedia.org/wiki/Q-learning
