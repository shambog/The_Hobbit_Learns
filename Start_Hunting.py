# Execute this file.
from Map_Environment import Map
from Learning_Engine import QLearningTable


def update():
    for attempt in range(50):

        # First Observation
        observation = env.reset()

        while True:

            # New Environment
            env.render()

            # Reinforcement Learning takes an action based on observation
            action = HobbitLearns.select_action(str(observation)) 

            # Reinforcement Learning taks action and gets next observation and reward
            newObservation, reward, done = env.step(action)

            # Learns
            HobbitLearns.learn(str(observation), action, reward, str(newObservation))

            # Latest Observation
            observation = newObservation

            # Break
            if done:
                break

    # Hunt Stops
    print('Endgame')
    env.destroy()

if __name__ == "__main__":
    env = Map()
    HobbitLearns = QLearningTable(actions=list(range(env.total_actions)))

    env.after(100, update)
    env.mainloop()