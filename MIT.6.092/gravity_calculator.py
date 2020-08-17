class GravityCalculator:
    def __init__(self, gravity=-9.81, initial_velocity=0, falling_time=0, initial_position=0, final_position=0):
        self.gravity = gravity
        self.initial_velocity = initial_velocity
        self.falling_time = falling_time
        self.initial_position = initial_position
        self.final_position = final_position

    def calculate(self):
        self.final_position = 0.5 * self.gravity * self.falling_time**2 + \
                                (self.initial_velocity*self.falling_time) + \
                                (self.initial_velocity)
        return self.__str__()

    def __str__(self):
        print(f'The object position after {self.falling_time} seconds is {self.final_position} m.')


gc = GravityCalculator(falling_time=10)
gc.calculate()