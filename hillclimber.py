from solution import SOLUTION
import constants as c
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evovle(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()
        self.Print()

    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Print(self):
        print("\nFitness of parent:", self.parent.fitness,
              "| Fitness of child:", self.child.fitness)

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child
        # print("Fitness of parent: ", self.parent.fitness)
        # print("Fitness of parent: ",self.child.fitness)
        # exit()