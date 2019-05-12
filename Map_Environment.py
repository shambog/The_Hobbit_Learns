
import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


# Resolution
UNIT = 50  

# MAP HEIGHT
MAP_H = 8  

# MAP WIDTH
MAP_W = 8  


class Map(tk.Tk, object):
    def __init__(self):
        super(Map, self).__init__()
        self.action_space = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.total_actions = len(self.action_space)
        self.title('Map')
        self.geometry('{0}x{1}'.format(MAP_H * UNIT, MAP_H * UNIT))
        self._build_map()

    def _build_map(self):
        self.canvas = tk.Canvas(self, bg='cyan2',
                           height=MAP_H * UNIT,
                           width=MAP_W * UNIT)

        # Grids
        for c in range(0, MAP_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAP_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAP_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAP_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # Starting Point
        starting = np.array([20, 20])

        # Obstacle-1

        obstacle1_center = starting + np.array([UNIT * 2, UNIT])
        self.obstacle1 = self.canvas.create_rectangle(
            obstacle1_center[0] - 10, obstacle1_center[1] - 15,
            obstacle1_center[0] + 10, obstacle1_center[1] + 15,
            fill='orange')

        # Obstacle-2

        obstacle2_center = starting + np.array([UNIT, UNIT * 2])
        self.obstacle2 = self.canvas.create_rectangle(
            obstacle2_center[0] - 10, obstacle2_center[1] - 15,
            obstacle2_center[0] + 10, obstacle2_center[1] + 15,
            fill='orange')

        # Obstacle-3

        obstacle3_center = starting + np.array([UNIT, UNIT * 3])
        self.obstacle3 = self.canvas.create_rectangle(
            obstacle3_center[0] - 10, obstacle3_center[1] - 15,
            obstacle3_center[0] + 10, obstacle3_center[1] + 15,
            fill='orange')
            
            
        # Obstacle-4   

        obstacle4_center = starting + np.array([UNIT * 5, UNIT * 6])
        self.obstacle4 = self.canvas.create_rectangle(
            obstacle4_center[0] - 10, obstacle4_center[1] - 15,
            obstacle4_center[0] + 10, obstacle4_center[1] + 15,
            fill='orange')

        
        # Treasure

        theTreasure = starting + UNIT * 2
        self.oval = self.canvas.create_oval(
            theTreasure[0] - 15, theTreasure[1] - 15,
            theTreasure[0] + 15, theTreasure[1] + 15,
            fill='green')

        
        # The Hobbit

        self.rect = self.canvas.create_rectangle(
            starting[0] - 15, starting[1] - 15,
            starting[0] + 15, starting[1] + 15,
            fill='red')

        # Packing Everything
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        starting = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
            starting[0] - 15, starting[1] - 15,
            starting[0] + 15, starting[1] + 15,
            fill='red')
        # return observation
        return self.canvas.coords(self.rect)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # UP
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # DOWN
            if s[1] < (MAP_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # RIGHT
            if s[0] < (MAP_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # LEFT
            if s[0] > UNIT:
                base_action[0] -= UNIT

        # Move The Hobbit
        self.canvas.move(self.rect, base_action[0], base_action[1])  
        
        # Next State
        s_ = self.canvas.coords(self.rect)  

        # Rewards
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
            s_ = 'terminal'
        elif s_ in [self.canvas.coords(self.obstacle1), self.canvas.coords(self.obstacle2), self.canvas.coords(self.obstacle3), self.canvas.coords(self.obstacle4)]:
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False

        return s_, reward, done

    def render(self):
        time.sleep(0.1)
        self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            s, r, done = env.step(a)
            if done:
                break

if __name__ == '__main__':
    env = Map()
    env.after(100, update)
    env.mainloop()