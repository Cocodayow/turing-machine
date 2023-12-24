class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  # Convert the input string to a list
        self.head = 0  # Head position
        self.state = 'q0'  # Initial state

    def move_left(self):
        if self.head == 0:
            self.tape.insert(0, '_')
        else:
            self.head -= 1

    def move_right(self):
        self.head += 1
        if self.head == len(self.tape):
            self.tape.append('_')

    def write(self, symbol):
        self.tape[self.head] = symbol

    def read(self):
        if self.head >= len(self.tape):
            return '_'
        return self.tape[self.head]

    def run(self):

        if self.tape[0] == "_":
            print("State:", self.state)
            print("Tape: ", "".join(self.tape))
            print("Head: ", " " * self.head + "^")
            print("--------------------")
            print("Computation finished.")
            return

        transitions = {
            ('q0', 'a'): ('q1', 'a', 'R'),  # Transition to q1, replace 'a' with 'a', move right
            ('q0', 'b'): ('q1', 'b', 'R'),  # Transition to q1, replace 'b' with 'b', move right
            ('q1', 'a'): ('q3', 'a', 'R'),  # Transition to q3, replace 'a' with 'a', move right
            ('q1', 'b'): ('q3', 'b', 'R'),  # Transition to q3, replace 'b' with 'b', move right
            ('q1', '_'): ('q2', 'a', 'R'),  # Transition to q2, replace '_' with 'a', move right
            ('q2', '_'): ('q2', '', 'R'),  # Stay in q2, replace '_' with '', move right
            ('q3', 'a'): ('q1', 'a', 'R'),  # Transition to q1, replace 'a' with 'a', move right
            ('q3', 'b'): ('q1', 'b', 'R'),  # Transition to q1, replace 'b' with 'b', move right
            ('q3', '_'): ('q4', '', 'L'),  # Transition to q4, replace '_' with '', move left
            ('q4', 'a'): ('q5', '', 'R'),  # Transition to q5, replace 'a' with '', move right
            ('q4', 'b'): ('q5', '', 'R'),  # Transition to q5, replace 'b' with '', move right
            ('q5', '_'): ('q5', '', 'R'),  # Stay in q5, replace '_' with '', move right
            ('q6', '_'): ('q6', '', 'R'),  # Stay in q6, replace '_' with '', move right
        }
        while (self.state != 'q2') and (self.state != 'q5'):
            symbol = self.read()
            print("State:", self.state)
            print("Tape: ", "".join(self.tape))
            print("Head: ", " " * self.head + "^")
            print("--------------------")

            if (self.state, symbol) in transitions:
                new_state, new_symbol, direction = transitions[(self.state, symbol)]
                self.state = new_state
                self.write(new_symbol)
                if direction == 'L':
                    self.move_left()
                else:
                    self.move_right()
            else:
                print("Error: No transition defined for state '{}' and symbol '{}'".format(self.state, symbol))
                return
            print("State:", self.state)
            print("Tape: ", "".join(self.tape))
            print("Head: ", " " * self.head + "^")
            print("--------------------")
            print("Computation finished.")


# Example usage
input_string = "a"

tm = TuringMachine(input_string)
tm.run()