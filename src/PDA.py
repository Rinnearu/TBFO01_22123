class PDA:
    def __init__(self):
        self.states = set()
        self.input_symbols = set()
        self.stack_symbols = set()
        self.start_state = ''
        self.stack = []
        self.accept_states = set()
        self.transitions = {}

    def INFOTOP(self):
        return self.stack[-1]
    
    def add_transition(self, current_state, input_symbol, stack_symbol, next_state, stack_operation):
        key = (current_state, input_symbol, stack_symbol)
        value = (next_state, stack_operation)

        if key not in self.transitions:
            self.transitions[key] = []

        if value not in self.transitions[key]:
            self.transitions[key].append(value)

    def read_pda(self, filename):
        with open(filename,'r') as file:
            line = file.readline().strip()
            for i in range(6):
                while line[0] == '#':
                    line = file.readline().strip()
                if (i == 0):
                    self.states = set(line.split())
                elif (i == 1):
                    self.input_symbols = set(line.split())
                elif (i == 2):
                    self.stack_symbols = set(line.split())
                elif (i == 3):
                    self.start_state = line.split()[0]
                elif (i == 4):
                    self.stack.extend(list(line.split()))
                else:
                    self.accept_states = set(line.split())
                line = file.readline().strip()

            while (len(line) > 0):
                while line[0] == '#':
                    line = file.readline().strip()
                parts = line.split()
                if (len(parts) >= 5):
                    self.add_transition(parts[0],parts[1],parts[2],parts[3],parts[4])
                line = file.readline().strip()

    # def simulate(self, input):
        