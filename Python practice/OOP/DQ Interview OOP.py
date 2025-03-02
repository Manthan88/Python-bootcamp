import random

class RandomAnalyzer:
    def __init__(self, lower_bound, upper_bound, n):
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.n = n
        self.RandomList = [random.randint(self.lower_bound, self.upper_bound) for _ in range(self.n)]
        
    def display_list(self):
            print(self.RandomList)

    def mean(self):
         if len(self.RandomList) == 0:
            return sum(self.RandomList)/len(self.RandomList)
         else: 
            0 
    
    def diff(self):
         second_smallest = self.RandomList.sort[1]
         second_largest = self.RandomList.sort[-2]
         return second_largest - second_smallest
    
