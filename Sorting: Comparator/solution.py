from functools import cmp_to_key

class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        print(f'{self.name} {self.score}')

    def comparator(a, b):
        if a.score == b.score:
            if a.name > b.name:
                return 1
            elif b.name > a.name:
                return -1
            else:
                return 0
        return b.score - a.score
        

