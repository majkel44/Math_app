import tkinter as tk

def enter_number():
    while True:
        try:
            number = float(input("Enter your number: "))
            return number
        except ValueError:
            print("That's not a number! Try again.")


class Calculator(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.output = 0.0
        self.running = True
        self.outputs = []
        self.operations = {"1":lambda: setattr(self,'output',enter_number()),
                           "2":self._addition,
                           "3":self._subtraction,
                           "4":self._multiplication,
                           "5":self._division,
                           "6":self._power,
                           "7":self._root,
                           "8":self._display_outputs,
                           "9":lambda: setattr(self,'running',False),}

    def run(self):
        self.running = True
        self.menu.pack_forget()
        self.pack(expand=True, fill="both")
        square = tk.Button(self, text="Close", command=self._close)
        square.pack(expand=True, fill="both")
        #square.place(relwidth=0.7, relx=0.5, rely=1 / 7, anchor="n")
        # while self.running:
        #     print("\nYour number is:", self.output,
        #           "\n\nWhat operation do you want to perform on your number?\n"
        #           "1) Change the number\n2) Addition\n3) Subtraction\n"
        #           "4) Multiplication\n5) Division\n6) Power\n"
        #           "7) Root\n8) Display history\n"
        #           "9) Leave the app\n")
        #     operation = input("Enter your choice: ")
        #     action = self.operations.get(operation)
        #     if action is None:
        #         print("That is not an option. Try again.")
        #         continue
        #     action()

    def _close(self):
        self.pack_forget()
        self.menu.pack(expand=True, fill="both")

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
        # print("The root of what degree do you want to use on your number?")
        # number = enter_number()
        # if self.output < 0:
        #     if number % 2 == 0:
        #         print("You cannot use this root on negative number!")
        #         return
        #     self.output = -(-self.output) ** (1/number)
        #     self.outputs.append(self.output)
        #     return
        self.output = self.output ** (1/2)
        self.outputs.append(self.output)

    def _display_outputs(self):
        print("\nYour previous outputs are:")
        print(self.outputs)