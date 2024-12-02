import tkinter as tk

class SimpleCalculator:
    def _init_(self):
        self.window = tk.Tk()
        self.window.title("Simple Calculator")

        self.entry = tk.Entry(self.window)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("/", 4, 3),
        ]

        for text, row, column in buttons:
            button = tk.Button(self.window, text=text, command=lambda t=text: self.click(t))
            button.grid(row=row, column=column)

        self.window.mainloop()

    def click(self, text):
        if text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, text)

if __name__== "_main_":
    calculator = SimpleCalculator()