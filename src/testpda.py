from PDA import PDA

def main():
    my_pda = PDA()

    my_pda.read_pda('PDA.txt')

    print(my_pda.states)
    print(my_pda.input_symbols)
    print(my_pda.stack_symbols)
    print(my_pda.start_state)
    print(my_pda.start_stack)
    print(my_pda.accept_states)
    print(my_pda.transitions)

main()