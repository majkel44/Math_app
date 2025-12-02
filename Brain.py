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

    def run(self):
        while True:
            print("\nYour number is:", self.output,
                  "\n\nWhat operation do you want to perform on your number?\n"
                  "1) Addition\n2) Subtraction\n3) Multiplication\n"
                  "4) Division\n5) Change the number\n6) Leave the app")
            operation = input()
            if operation == "1":
                self.__addition()
            elif operation == "2":
                self.__subtraction()
            elif operation == "3":
                self.__multiplication()
            elif operation == "4":
                self.__division()
            elif operation == "5":
                self.output = enter_number()
            elif operation == "6":
                print("\n You're leaving the calculator. Goodbye!")
                break
            else:
                print("That is not an option. Try again.")

    def __addition(self):
        print("What number do you want to add?")
        number = enter_number()
        self.output = self.output + number

    def __subtraction(self):
        print("What number do you want to subtract?")
        number = enter_number()
        self.output = self.output - number

    def __multiplication(self):
        print("What number do you want to multiply by?")
        number = enter_number()
        self.output = self.output * number

    def __division(self):
        print("What number do you want to divide by?")
        while True:
            number = enter_number()
            if number != 0:
                break
            else:
                print("You cannot divide by 0! Try again.")
        self.output = self.output / number


def main():
    print("\nWelcome to the Brain!\nLets start calculating!\n")
    calc = Calculator()
    calc.run()


if __name__ == '__main__':
    main()