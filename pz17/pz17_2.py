import tkinter as tk
import math

def TriangleP(a):
    return 3*a, 2*a*math.sqrt(3/4)

def calculate():
    a = int(entry.get())
    perimeter, area = TriangleP(a)
    result_text.set(f"Периметр равена {perimeter}\nПлощадь равна {area}")

root = tk.Tk()
root.title("Треугольник")
root.geometry("300x200")

label = tk.Label(root, text="Введите сторону треугольника:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Вычислить", command=calculate)
button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop()
