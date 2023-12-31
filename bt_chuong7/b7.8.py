import tkinter as tk
window = tk.Tk()
window.title("Liệt kê các ước của một số nguyên")
window.geometry("400x200")
tk.Label(window, text="Nhập số nguyên N:").grid(row=0, column=0)

n_entry = tk.Entry(window, width=30)
n_entry.grid(row=0, column=1)

def calculate_divisors():
    N = int(n_entry.get())
    uoc_so = []
    for i in range(1, N+1):
        if N % i == 0:
            uoc_so.append(i)
    result_label.config(text="Các ước của " + str(N) + " là: " + str(uoc_so))

calculate_button = tk.Button(window, text="Liệt kê các ước", command=calculate_divisors)
calculate_button.grid(row=1, column=0)
result_label = tk.Label(window, text="")
result_label.grid(row=1, column=1)
window.mainloop()