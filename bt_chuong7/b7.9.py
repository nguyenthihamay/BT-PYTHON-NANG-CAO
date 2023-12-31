import tkinter as tk
from math import gcd
window = tk.Tk()
window.title("Tính GCD và LCM")
window.geometry("400x200")
tk.Label(window, text="Nhập số nguyên a:").grid(row=0, column=0)
a_entry = tk.Entry(window, width=30)
a_entry.grid(row=0, column=1)

tk.Label(window, text="Nhập số nguyên b:").grid(row=1, column=0)

b_entry = tk.Entry(window, width=30)
b_entry.grid(row=1, column=1)

# Tạo một hàm để tính GCD và LCM của a và b
def calculate_gcd_lcm():
    a = int(a_entry.get())
    b = int(b_entry.get())

    # Tính GCD và LCM của a và b
    gcd_value = gcd(a, b)
    lcm_value = abs(a * b) // gcd_value

    # Hiển thị kết quả
    result_label.config(text=f"GCD của {a} và {b} là {gcd_value}\nLCM của {a} và {b} là {lcm_value}")

# Tạo một nút tính toán để tính GCD và LCM của a và b
calculate_button = tk.Button(window, text="Tính GCD và LCM", command=calculate_gcd_lcm)
calculate_button.grid(row=2, column=0)
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=1)

# Hiển thị cửa sổ
window.mainloop()
