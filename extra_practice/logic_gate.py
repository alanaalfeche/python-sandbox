'''
Inheritance relationships:
IS-A relationship -- inheritance
HAS-A relationship -- no inheritance
'''
class LogicGate:

    def __init__(self, val):
        self.label = val
        self.output = None
    
    def get_label(self):
        return self.label
    
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, val):
        # Child class constructors need to call parent class constructors and then move on to their own distinguishing data.
        LogicGate.__init__(self, val)

        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        return int(input("Enter Pin A input for gate "+ self.get_label()+"--->"))

    def get_pinB(self):
        return int(input("Enter Pin B input for gate "+ self.get_label()+"--->"))

    def set_next_pin(self, source): 
        if self.pinA == None:
            self.pinA = source 
        else:
            if self.pinB == None:
                self.pinB = source 
            else:
                print("No empty pins on this gate")

class UnaryGate(LogicGate):

    def __init__(self, val):
        # Can be replaced with `super(UnaryGate,self).__init__(n)`
        LogicGate.__init__(self, val)

        self.pin = None
    
    def get_pin(self):
        return int(input("Enter Pin input for gate "+ self.get_label()+"--->"))

    def set_next_pin(self, source): 
        if self.pin == None:
            self.pin = source 
        else:
            print("No empty pins on this gate")

class AndGate(BinaryGate):

    def __init__(self, val):
        super(AndGate, self).__init__(val)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        return 1 if (a == 1 and b == 1) else 0

class OrGate(BinaryGate):

    def __init__(self, val):
        super(OrGate, self).__init__(val)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        return 1 if (a == 1 or b == 1) else 0

    def size(self):
        return 'hello'

class NotGate(UnaryGate):

    def __init__(self, val):
        super(NotGate, self).__init__(val)

    def perform_gate_logic(self):
        return 0 if self.get_pin() else 1

# g1 = AndGate("G1")
# print(g1.get_output())

# g2 = OrGate("G2")
# print(g2.get_output())

# g3 = NotGate("G3")
# print(g3.get_output())

