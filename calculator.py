import tkinter as tk


class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title(" Calculator")
        self.root.geometry("340x480")
        self.root.config(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.expression = ""

        # Input Display Screen
        self.text_input = tk.StringVar()
        self.display = tk.Entry(
            root,
            font=("Arial", 22, "bold"),
            textvariable=self.text_input,
            bg="#2d2d2d",
            fg="#ffffff",
            bd=0,
            justify="right",
        )
        self.display.pack(fill="both", ipady=20, padx=15, pady=20)

        # Buttons Frame
        self.btn_frame = tk.Frame(root, bg="#1e1e1e")
        self.btn_frame.pack()

        # Button Layout Configuration
        buttons = [
            ("C", 1, 0, "#ff4d4d", "#ffffff"),
            ("(", 1, 1, "#444444", "#ffffff"),
            (")", 1, 2, "#444444", "#ffffff"),
            ("/", 1, 3, "#ff9f0a", "#ffffff"),
            ("7", 2, 0, "#333333", "#ffffff"),
            ("8", 2, 1, "#333333", "#ffffff"),
            ("9", 2, 2, "#333333", "#ffffff"),
            ("*", 2, 3, "#ff9f0a", "#ffffff"),
            ("4", 3, 0, "#333333", "#ffffff"),
            ("5", 3, 1, "#333333", "#ffffff"),
            ("6", 3, 2, "#333333", "#ffffff"),
            ("-", 3, 3, "#ff9f0a", "#ffffff"),
            ("1", 4, 0, "#333333", "#ffffff"),
            ("2", 4, 1, "#333333", "#ffffff"),
            ("3", 4, 2, "#333333", "#ffffff"),
            ("+", 4, 3, "#ff9f0a", "#ffffff"),
            ("0", 5, 0, "#333333", "#ffffff"),
            (".", 5, 1, "#333333", "#ffffff"),
            ("⌫", 5, 2, "#444444", "#ffffff"),
            ("=", 5, 3, "#34c759", "#ffffff"),
        ]

        # Create and place buttons using a loop
        for btn_text, row, col, bg_color, fg_color in buttons:
            self.create_button(
                btn_text, row, col, bg_color, fg_color, span=(1, 1)
            )

    def create_button(
        self, text, row, col, bg_color, fg_color, span=(1, 1)
    ):
        button = tk.Button(
            self.btn_frame,
            text=text,
            font=("Arial", 16, "bold"),
            bg=bg_color,
            fg=fg_color,
            bd=0,
            activebackground="#555555",
            activeforeground="#ffffff",
            command=lambda: self.on_button_click(text),
        )
        button.grid(
            row=row, column=col, columnspan=span[1], ipadx=18, ipady=12, padx=5, pady=5
        )

    def on_button_click(self, item):
        if item == "C":
            self.expression = ""
            self.text_input.set("")
        elif item == "⌫":
            self.expression = self.expression[:-1]
            self.text_input.set(self.expression)
        elif item == "=":
            try:
                # Evaluate the mathematical expression safely
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except Exception:
                self.text_input.set("Error")
                self.expression = ""
        else:
            self.expression += str(item)
            self.text_input.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()