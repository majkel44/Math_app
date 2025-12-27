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
        self.input = ""
        self.running = True
        self.outputs = []
        self.operations = {"1":lambda: setattr(self,'output',enter_number()),
                           "2":self._addition,
                           "3":self._subtraction,
                           "4":self._multiplication,
                           "5":self._division,
                           "6":self._power,
                           "7":self._root,
                           "8":self._display_outputs}
                           #"9":lambda: setattr(self,'running',False),}

    def run(self):
        #self.running = True
        self.main_menu.pack_forget()
        self.pack(expand=True, fill="both")

        display = tk.Frame(self, bg="#1e1f1f")
        options = tk.Frame(self, bg="#2e3030")
        menu = tk.Frame(self, bg="#1e1f1f")
        display.pack(expand=True, fill="both")
        options.pack(expand=True, fill="both")
        menu.pack(expand=True, fill="both")

        display_position = tk.Frame(display, bg="#1e1f1f")
        options_position = tk.Frame(options, bg="#2e3030")
        menu_position = tk.Frame(menu, bg="#1e1f1f")

        input_label = tk.Label(display_position, text="Input: " + self.input)
        output_label = tk.Label(display_position, text="Output: " + str(self.output))

        add_button = tk.Button(options_position, text="+", command=self._addition, borderwidth=2, relief="raised")
        subtract_button = tk.Button(options_position, text="_", command=self._subtraction, borderwidth=2, relief="raised")
        multiply_button = tk.Button(options_position, text="*", command=self._multiplication, borderwidth=2, relief="raised")
        divide_button = tk.Button(options_position, text="/", command=self._division, borderwidth=2, relief="raised")
        power_button = tk.Button(options_position, text="^", command=self._power, borderwidth=2, relief="raised")
        root_button = tk.Button(options_position, text="sqrt", command=self._root, borderwidth=2, relief="raised")

        zero_button = tk.Button(options_position, text="0", command=self._root, borderwidth=2, relief="raised")
        one_button = tk.Button(options_position, text="1", command=self._root, borderwidth=2, relief="raised")
        two_button = tk.Button(options_position, text="2", command=self._root, borderwidth=2, relief="raised")
        three_button = tk.Button(options_position, text="3", command=self._root, borderwidth=2, relief="raised")
        four_button = tk.Button(options_position, text="4", command=self._root, borderwidth=2, relief="raised")
        five_button = tk.Button(options_position, text="5", command=self._root, borderwidth=2, relief="raised")
        six_button = tk.Button(options_position, text="6", command=self._root, borderwidth=2, relief="raised")
        seven_button = tk.Button(options_position, text="7", command=self._root, borderwidth=2, relief="raised")
        eight_button = tk.Button(options_position, text="8", command=self._root, borderwidth=2, relief="raised")
        nine_button = tk.Button(options_position, text="9", command=self._root, borderwidth=2, relief="raised")
        dot_button = tk.Button(options_position, text=".", command=self._root, borderwidth=2, relief="raised")

        history_button = tk.Button(menu_position, text="History", command=self._root, borderwidth=2, relief="raised")
        back_button = tk.Button(menu_position, text="Go back", command=lambda: self._close(), borderwidth=2, relief="ridge")

        display_position.place(relwidth=0.7, relx = 0.5, rely=0.3, anchor="n")
        options_position.place(relx=0.5, rely=0.2, anchor="n")
        menu_position.place(relx=0.5, rely=0.4, anchor="n")

        input_label.pack(padx=15, pady=10, expand=True, fill="x")
        output_label.pack(padx=15, pady=10, expand=True, fill="x")

        add_button.grid(row=0, column=0, padx=10, pady=10)
        subtract_button.grid(row=0, column=1, padx=10, pady=10)
        multiply_button.grid(row=1, column=0, padx=10, pady=10)
        divide_button.grid(row=1, column=1, padx=10, pady=10)
        power_button.grid(row=2, column=0, padx=10, pady=10)
        root_button.grid(row=2, column=1, padx=10, pady=10)

        history_button.grid(row=0, column=0, padx=10, pady=10)
        back_button.grid(row=0, column=1, padx=15, pady=10)


    def update_input(self,x):
        self.input += self.input + str(x)

    def _close(self):
        self.pack_forget()
        self.main_menu.pack(expand=True, fill="both")

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