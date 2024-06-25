import tkinter as tk

root = tk.Tk()
root.title("String Generator")
root.geometry("300x200")

label_number = tk.Label(root, text="Введите число:")
label_number.grid(row=0, column=0, padx=5, pady=5)

entry_number = tk.Entry(root)
entry_number.grid(row=0, column=1, padx=5, pady=5)

label_symbol = tk.Label(root, text="Введите символ:")
label_symbol.grid(row=1, column=0, padx=5, pady=5)

entry_symbol = tk.Entry(root)
entry_symbol.grid(row=1, column=1, padx=5, pady=5)

def generate_string():
    number = int(entry_number.get())
    symbol = entry_symbol.get()

    result = ""
    for _ in range(number):
        result += symbol

    result_label.config(text=f"Результат: {result}")

generate_button = tk.Button(root, text="Сгенерировать", command=generate_string)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
