# 1.1.3
import Calculator
import tkinter as tk
from tkinter import ttk

def gui_declaration(tk_root, calc):
    tk_root.title("Brain")
    tk_root.geometry("400x600")
    tk_root.resizable(False, False)
    tk_root.configure(background="#eeeeee")

    menu = tk.Frame(master=tk_root)
    menu.pack(expand=True, fill="both")
    options = tk.Frame(menu, bg="#dddddd")
    options.place(relwidth=0.7, relx=0.5, rely=1/7, anchor="n")

    calc_button = ttk.Button(options, text="Calculator", command=calc.run, width=40)
    dummy_button = ttk.Button(options, text="Dummy", width=40)
    close_button = ttk.Button(options, text="Close", command=tk_root.destroy, width=40)

    y_distance = 5
    calc_button.pack(pady=y_distance)
    dummy_button.pack(pady=y_distance)
    close_button.pack(pady=y_distance)

    calc.menu = menu

def main():
    print("\nWelcome to the Brain!\nLets start calculating!\n")
    root = tk.Tk()
    calc = Calculator.Calculator(root)
    gui_declaration(root, calc)
    root.mainloop()

if __name__ == '__main__':
    main()