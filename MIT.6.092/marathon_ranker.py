class MarathonRanker:
    def __init__(self, racers):
        self.racers = racers

    
    def rank(self):
        ranked = sorted(self.racers)
        
        self.return_first(ranked[0])
        self.return_second(ranked[1])

    
    def return_first(self, first_idx):
        return self.__str__(self.racers[first_idx], 1)

    
    def return_second(self, second_idx):
        return self.__str__(self.racers[second_idx], 2)


    def __str__(self, name, placement):
        print(f'Ranked #{placement}: {name}')


racers = {341: 'Elena', 273: 'Thomas', 278: 'Hamilton', 329: 'Suzie', 445: 'Phil', 402: 'Matt', 388: 'Alex', 275: 'Emma', 243: 'John', 334: 'James', 412: 'Jane', 393: 'Emily', 299: 'Daniel', 343: 'Neda', 317: 'Aaron', 265: 'Kate'}
mr = MarathonRanker(racers)
mr.rank()