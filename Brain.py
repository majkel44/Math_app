class Calculator:
    def __init__(self):
        calculate = 1
        self.output = self.enter_number()
        while calculate:
            print("\nYour number is:", self.output,
                  "\n\nWhat operation do you want to perform on your number?\n"
                  "1) Addition\n2) Subtraction\n3) Multiplication\n"
                  "4) Division\n5) Change the number\n6) Leave the app")
            operation = input()
            if operation == "1":
                self.addition()
            elif operation == "2":
                self.subtraction()
            elif operation == "3":
                self.multiplication()
            elif operation == "4":
                self.division()
            elif operation == "5":
                self.output = self.enter_number()
            elif operation == "6":
                calculate = 0
            else:
                print("That is not an option. Try again.")

    def addition(self):
        print("What number do you want to add?")
        number = self.enter_number()
        self.output = self.output + number

    def subtraction(self):
        print("What number do you want to subtract?")
        number = self.enter_number()
        self.output = self.output - number

    def multiplication(self):
        print("What number do you want to multiply by?")
        number = self.enter_number()
        self.output = self.output * number

    def division(self):
        print("What number do you want to divide by?")
        while True:
            number = self.enter_number()
            if number != 0:
                break
            else:
                print("You cannot divide by 0! Try again.")
        self.output = self.output / number


    def enter_number(self):
        while True:
            try:
                number = float(input("Enter your number: "))
                return number
            except ValueError:
                print("That's not a number! Try again.")



def main():
    print("\nWelcome to the Brain!\nLets start calculating!\n")
    Calculator()


if __name__ == '__main__':
    main()