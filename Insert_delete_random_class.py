import random
from collections import defaultdict


class subOptimalSolution:
    def __init__(self):
        self.map = set()


    def insert(self, value: int):
        self.map.add(value)

    def remove(self, value: int):
        self.map.remove(value)


    def getRandom(self, value: int) -> int:
        return random.choice(value)


class optimalSolution:
    def __init__(self):
        self.map = defaultdict(set)
        self.self.value_to_index = []


    def insert(self, value: int):
        if value in self.map:
            return
        
        self.self.value_to_index.append(value)
        self.map[value].add(len(self.self.value_to_index) - 1) # mark newly added value at the last index within the list

    def remove(self, value: int):
        if value not in self.map:
            return
        
        index = next(iter(self.map[value]))

        last_val = self.self.value_to_index[-1]
        
        # swapping
        self.self.value_to_index[index] = last_val
        self.map[last_val].add(index)
        self.map[last_val].remove(len(self.self.value_to_index) - 1)

        # Remove the value
        self.self.value_to_index.pop()
        self.map[value].remove(index)

        if not self.map[value]:
            del self.map[value]



    def getRandom(self, value: int) -> int:
        return random.choice(value)



    

