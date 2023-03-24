import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agent_pos = (0, 0)
        self.wumpus_alive = True
        self.generate_world()
    
    def generate_world(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in [(0, 2), (2, 2), (3, 3)]:
                    self.grid[i][j] = "pit"
                elif (i, j) in [(0, 1), (0, 3), (1, 2),(2, 3), (3, 2)]:
                    self.grid[i][j] = "breeze"
                elif (i, j) in [(1,0),(3,0)]:
                    self.grid[i][j] = "stench"
                elif (i, j) in [(2,0)]:
                    self.grid[i][j] = "wumpus"
                elif (i, j) in [(2,1)]:
                    self.grid[i][j] = "gold"
                elif (i, j) in [(0,0)]:
                    self.grid[i][j] = "start position"
                elif (i, j) in [(1,1),(1,3),(3,1)]:
                    self.grid[i][j] = "safe position"
        print("\n\nThe Wumpus World is: ")
        for i in range(len(self.grid)):
            print(self.grid[i])
        print("\n\n")
        
        
    def percept(self):
        i, j = self.agent_pos
        percept = []
        if self.grid[i][j] == "breeze":
            percept.append("breeze")
        if self.grid[i][j] == "stench":
            percept.append("stench")
        if self.grid[i][j] == "safe position":
            percept.append("safe position")
        if self.grid[i][j] == "gold":
            percept.append("gold")
        if i == 2 and j == 0 and self.wumpus_alive:
            percept.append("wumpus")
        return percept
    
    def move_agent(self, action):
        if action == "up" and self.agent_pos[0] > 0:
            self.agent_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
        elif action == "down" and self.agent_pos[0] < self.size - 1:
            self.agent_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
        elif action == "left" and self.agent_pos[1] > 0:
            self.agent_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
        elif action == "right" and self.agent_pos[1] < self.size - 1:
            self.agent_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
    
    def shoot_arrow(self):
        i, j = self.agent_pos
        if i == 0 and j < self.size - 1:
            for k in range(j+1, self.size):
                if self.grid[i][k] == "wumpus":
                    self.wumpus_alive = False
                elif self.grid[i][k] == "pit":
                    break
        elif i == self.size - 1 and j < self.size - 1:
            for k in range(j+1, self.size):
                if self.grid[i][k] == "wumpus":
                    self.wumpus_alive = False
                    break
                elif self.grid[i][k] == "pit":
                    break
        elif j == 0 and i < self.size - 1:
            for k in range(i+1, self.size):
                if self.grid[k][j] == "wumpus":
                    self.wumpus_alive = False
                    break
                elif self.grid[k][j] == "pit":
                    break
        elif j == self.size - 1 and i < self.size - 1:
            for k in range(i+1, self.size):
                if self.grid[k][j] == "wumpus":
                    self.wumpus_alive = False
                    break
                elif self.grid[k][j] == "pit":
                    break
    
    def run(self):
        while True:
            percept = self.percept()
            print("Current position:", percept ,"and current location: ",self.agent_pos)
            action = input("enter Action(up/down/left/right/shoot/quit): ")
            if action == "up" or action == "down" or action == "left" or action == "right":
                self.move_agent(action)
            elif action == "shoot":
                self.shoot_arrow()
            elif action == "quit":
                print("Goodbye!")
                break
            else:
                print("Invalid action!")
                continue
            print("\n\n")
            i, j = self.agent_pos
            if self.grid[i][j] == "pit":
                print("You fell into a pit! Game over.")
                break
            elif self.grid[i][j] == "wumpus" and self.wumpus_alive:
                print("You were eaten by the wumpus! Game over.")
                break
            elif not self.wumpus_alive and self.grid[i][j] == "wumpus":
                print("You killed the wumpus! Congratulations, you won!")
                break
            elif self.grid[i][j] == "gold":
                print("You found the gold and exit! Congratulations, you won!")
                break

world = WumpusWorld()
world.run()
