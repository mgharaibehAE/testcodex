# Simple calculator app using tkinter
import tkinter as tk
from functools import partial

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Python Calculator')
        self.resizable(False, False)
        self._build_widgets()
        self.expression = ''

    def _build_widgets(self):
        self.display = tk.Entry(self, font=('Arial', 20), bd=5, relief=tk.RIDGE, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for idx, text in enumerate(buttons):
            cmd = partial(self.on_button_click, text)
            tk.Button(self, text=text, width=5, height=2, font=('Arial', 18), command=cmd).grid(
                row=1 + idx // 4, column=idx % 4, padx=2, pady=2
            )

        tk.Button(self, text='C', width=5, height=2, font=('Arial', 18), command=self.clear).grid(row=5, column=0, padx=2, pady=2)
        tk.Button(self, text='←', width=5, height=2, font=('Arial', 18), command=self.backspace).grid(row=5, column=1, padx=2, pady=2)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, 'Error')
            self.expression = ''

    def clear(self):
        self.expression = ''
        self.display.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)


def main():
    calc = Calculator()
    calc.mainloop()


if __name__ == '__main__':
    main()
