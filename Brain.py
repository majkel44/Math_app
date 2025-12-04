def enter_number():
    while True:
        try:
            number = float(input("Enter your number: "))
            return number
        except ValueError:
            print("That's not a number! Try again.")


class Calculator:
    def __init__(self):
        self.output = 0.0
        self.running = True
        self.outputs = []
        self.operations = {"1":self._addition,
                           "2":self._subtraction,
                           "3":self._multiplication,
                           "4":self._division,
                           "5":self._power,
                           "6":self._root,
                           "7":lambda: setattr(self,'output',enter_number()),
                           "8":lambda: setattr(self,'running',False)}

    def run(self):
        while self.running:
            print("\nYour number is:", self.output,
                  "\n\nWhat operation do you want to perform on your number?\n"
                  "1) Addition\n2) Subtraction\n3) Multiplication\n"
                  "4) Division\n5) Power\n6) Root\n"
                  "7) Change the number\n8) Leave the app\n")
            operation = input("Enter your choice: ")
            action = self.operations.get(operation)
            if action is None:
                print("That is not an option. Try again.")
                continue
            action()

    def _addition(self):
        print("What number do you want to add?")
        number = enter_number()
        self.output = self.output + number
        self.outputs.append(self.output)

    def _subtraction(self):
        print("What number do you want to subtract?")
        number = enter_number()
        self.output = self.output - number
        self.outputs.append(self.output)

    def _multiplication(self):
        print("What number do you want to multiply by?")
        number = enter_number()
        self.output = self.output * number
        self.outputs.append(self.output)

    def _division(self):
        print("What number do you want to divide by?")
        while True:
            number = enter_number()
            if number != 0:
                break
            else:
                print("You cannot divide by 0! Try again.")
        self.output = self.output / number
        self.outputs.append(self.output)

    def _power(self):
        print("To what power do you want to increase your number?")
        number = enter_number()
        self.output = self.output ** number
        self.outputs.append(self.output)

    def _root(self):
        print("The root of what degree do you want to use on your number?")
        number = enter_number()
        if self.output < 0:
            if number % 2 == 0:
                print("You cannot use this root on negative number!")
                return
            self.output = -(-self.output) ** (1/number)
            self.outputs.append(self.output)
            return
        self.output = self.output ** (1/number)
        self.outputs.append(self.output)


def main():
    print("\nWelcome to the Brain!\nLets start calculating!\n")
    calc = Calculator()
    calc.run()



if __name__ == '__main__':
    main()