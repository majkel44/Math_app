import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.output = tk.StringVar()
        self.input = tk.StringVar()
        self.running = True
        self.outputs = []

        self.display = tk.Frame(self, bg="#1e1f1f")
        self.options = tk.Frame(self, bg="#2e3030")
        self.menu = tk.Frame(self, bg="#1e1f1f")

        self.display_position = tk.Frame(self.display, bg="#1e1f1f")
        self.options_position = tk.Frame(self.options, bg="#2e3030")
        self.menu_position = tk.Frame(self.menu, bg="#1e1f1f")

        self.input_label = tk.Label(self.display_position, textvariable=self.input)
        self.output_label = tk.Label(self.display_position, textvariable=self.output)

        self.add_button = tk.Button(self.options_position, text="+", command=self._addition, borderwidth=2, relief="raised")
        self.subtract_button = tk.Button(self.options_position, text="-", command=self._subtraction, borderwidth=2, relief="raised")
        self.multiply_button = tk.Button(self.options_position, text="*", command=self._multiplication, borderwidth=2, relief="raised")
        self.divide_button = tk.Button(self.options_position, text="/", command=self._division, borderwidth=2, relief="raised")
        self.power_button = tk.Button(self.options_position, text="^", command=self._power, borderwidth=2, relief="raised")
        self.root_button = tk.Button(self.options_position, text="sqrt", command=self._root, borderwidth=2, relief="raised")
        self.reset_button = tk.Button(self.options_position, text="Reset", command=self._reset, borderwidth=2, relief="raised")

        self.zero_button = tk.Button(self.options_position, text="0", command=lambda: self.update_input("0"), borderwidth=2, relief="ridge")
        self.one_button = tk.Button(self.options_position, text="1", command=lambda: self.update_input("1"), borderwidth=2, relief="ridge")
        self.two_button = tk.Button(self.options_position, text="2", command=lambda: self.update_input("2"), borderwidth=2, relief="ridge")
        self.three_button = tk.Button(self.options_position, text="3", command=lambda: self.update_input("3"), borderwidth=2, relief="ridge")
        self.four_button = tk.Button(self.options_position, text="4", command=lambda: self.update_input("4"), borderwidth=2, relief="ridge")
        self.five_button = tk.Button(self.options_position, text="5", command=lambda: self.update_input("5"), borderwidth=2, relief="ridge")
        self.six_button = tk.Button(self.options_position, text="6", command=lambda: self.update_input("6"), borderwidth=2, relief="ridge")
        self.seven_button = tk.Button(self.options_position, text="7", command=lambda: self.update_input("7"), borderwidth=2, relief="ridge")
        self.eight_button = tk.Button(self.options_position, text="8", command=lambda: self.update_input("8"), borderwidth=2, relief="ridge")
        self.nine_button = tk.Button(self.options_position, text="9", command=lambda: self.update_input("9"), borderwidth=2, relief="ridge")
        self.dot_button = tk.Button(self.options_position, text=".", command=lambda: self.update_input("."), borderwidth=2, relief="raised")
        self.delete_button = tk.Button(self.options_position, text="<-", command=lambda: self.update_input("back"), borderwidth=2, relief="raised")

        self.history_button = tk.Button(self.menu_position, text="History", command=self._display_outputs, borderwidth=2, relief="raised")
        self.back_button = tk.Button(self.menu_position, text="Go back", command=lambda: self._close(), borderwidth=2, relief="ridge")

    def run(self):
        self.main_menu.pack_forget()
        self.pack(expand=True, fill="both")

        self.display.pack(expand=True, fill="both")
        self.options.pack(expand=True, fill="both")
        self.menu.pack(expand=True, fill="both")

        self.display_position.place(relwidth=0.7, relx = 0.5, rely=0.3, anchor="n")
        self.options_position.place(relx=0.5, rely=0.02, anchor="n")
        self.menu_position.place(relx=0.5, rely=0.4, anchor="n")

        self.input_label.pack(padx=15, pady=10, expand=True, fill="x")
        self.output_label.pack(padx=15, pady=10, expand=True, fill="x")

        self.output.set("0.0")

        self.zero_button.grid(row=3, column=1, padx=10, pady=10)
        self.one_button.grid(row=0, column=0, padx=10, pady=10)
        self.two_button.grid(row=0, column=1, padx=10, pady=10)
        self.three_button.grid(row=0, column=2, padx=10, pady=10)
        self.four_button.grid(row=1, column=0, padx=10, pady=10)
        self.five_button.grid(row=1, column=1, padx=10, pady=10)
        self.six_button.grid(row=1, column=2, padx=10, pady=10)
        self.seven_button.grid(row=2, column=0, padx=10, pady=10)
        self.eight_button.grid(row=2, column=1, padx=10, pady=10)
        self.nine_button.grid(row=2, column=2, padx=10, pady=10)
        self.dot_button.grid(row=3, column=0, padx=10, pady=10)
        self.delete_button.grid(row=3, column=2, padx=10, pady=10)

        self.add_button.grid(row=0, column=3, padx=10, pady=10)
        self.subtract_button.grid(row=0, column=4, padx=10, pady=10)
        self.multiply_button.grid(row=1, column=3, padx=10, pady=10)
        self.divide_button.grid(row=1, column=4, padx=10, pady=10)
        self.power_button.grid(row=2, column=3, padx=10, pady=10)
        self.root_button.grid(row=2, column=4, padx=10, pady=10)
        self.reset_button.grid(row=3, column=4, padx=10, pady=10)

        self.history_button.grid(row=0, column=0, padx=10, pady=10)
        self.back_button.grid(row=0, column=1, padx=15, pady=10)


    def update_input(self,x):
        current = self.input.get()
        if x == "back":
            if len(current) > 0:
                self.input.set(current[:-1])
                return
        self.input.set(current + str(x))

    def _reset(self):
        self.input.set("")
        self.output.set("0.0")

    def _close(self):
        self.pack_forget()
        self.main_menu.pack(expand=True, fill="both")

    def _addition(self):
        try:
            number_in = float(self.input.get())
        except:
            number_in = 0
        number_out = float(self.output.get())
        output = number_out + number_in
        self.output.set(str(output))
        self.input.set("")
        self.outputs.append(output)

    def _subtraction(self):
        try:
            number_in = float(self.input.get())
        except:
            number_in = 0
        number_out = float(self.output.get())
        output = number_out - number_in
        self.output.set(str(output))
        self.input.set("")
        self.outputs.append(output)

    def _multiplication(self):
        try:
            number_in = float(self.input.get())
        except:
            number_in = 0
        number_out = float(self.output.get())
        output = number_out * number_in
        self.output.set(str(output))
        self.input.set("")
        self.outputs.append(output)

    def _division(self):
        try:
            number_in = float(self.input.get())
        except:
            number_in = 0
        if number_in == 0:
            root = tk.Tk()
            root.title("Error")
            root.geometry("200x60")
            root.resizable(False, False)
            label = tk.Label(root, text="Cannot divide by 0.")
            button = tk.Button(root, text="Ok", command=root.destroy)
            label.pack()
            button.pack()
            return
        number_out = float(self.output.get())
        output = number_out / number_in
        self.output.set(str(output))
        self.input.set("")
        self.outputs.append(output)

    def _power(self):
        try:
            number_in = float(self.input.get())
        except:
            number_in = 0
        number_out = float(self.output.get())
        output = number_out ** number_in
        self.output.set(str(output))
        self.input.set("")
        self.outputs.append(output)

    def _root(self):
        number_out = float(self.output.get())
        output = number_out ** (1/2)
        self.output.set(str(output))
        self.input.set("")
        self.outputs.append(output)

    def _display_outputs(self):
        root = tk.Tk()
        root.title("Previous outputs")
        root.geometry("500x100")
        label = tk.Label(root, text=str(self.outputs))
        button = tk.Button(root, text="Close", command=root.destroy)
        label.pack()
        button.pack()