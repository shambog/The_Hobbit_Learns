
import numpy as np
import pandas as pd


class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, rd=0.9, eg=0.9):
        self.actions = actions  
        self.lr = learning_rate
        self.gamma = rd
        self.epsilon = eg
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def select_action(self, observation):
        self.check_state_exist(observation)
        
        # Action selection
        if np.random.uniform() < self.epsilon:
            # Take the best possible action
            state_action = self.q_table.loc[observation, :]
            # Random choice of action (if same values)
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            # Random choice of action
            action = np.random.choice(self.actions)
        return action

    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()  
        else:
            q_target = r
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # Add a new state
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )