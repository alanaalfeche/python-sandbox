from logic_gate import AndGate, OrGate, NotGate

class CircuitConnector:

    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate

        tgate.set_next_pin(self)

        def get_from(self):
            return self.fgate

        def get_to(self):
            return self.tgate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = CircuitConnector(g1,g3)
    c2 = CircuitConnector(g2,g3)
    c3 = CircuitConnector(g3,g4)
    print(g4.get_output())

main()

