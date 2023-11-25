class PDA:
    def __init__(self):
        self.states = set()
        self.input_symbols = set()
        self.stack_symbols = set()
        self.start_state = ''
        self.start_stack = ''
        self.accept_states = set()
        self.transitions = {}
    
    def add_transition(self, current_state, input_symbol, stack_symbol, next_state, stack_operation):
        key = (current_state, input_symbol, stack_symbol)
        value = (next_state, stack_operation)

        if key not in self.transitions:
            self.transitions[key] = value

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
                    self.start_stack = line
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

    def simulate(self, input):
        stack = list(self.start_stack)
        current_state = self.start_state

        for input_symbol in input:
            if (current_state, input_symbol, stack[-1]) in self.transitions:
                transition = self.transitions[(current_state, input_symbol, stack[-1])]
                stack.pop()
                if transition[1] != '$':
                    current_symbol = ''
                    for cc in reversed(transition[1]):
                        current_symbol = cc + current_symbol
                        if current_symbol in self.stack_symbols:
                            stack.append(current_symbol)
                            current_symbol = ''
                current_state = transition[0]
            else:
                return False
            
        return True