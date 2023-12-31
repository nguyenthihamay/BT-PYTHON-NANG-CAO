import tkinter as tk
window = tk.Tk()
window.title("Tính tổng các số từ 1 đến N")
window.geometry("400x200")
# Tạo một nhãn để yêu cầu người dùng nhập số nguyên N
tk.Label(window, text="Nhập số nguyên N:").grid(row=0, column=0)

# Tạo một hộp văn bản để người dùng nhập số nguyên N
n_entry = tk.Entry(window, width=30)
n_entry.grid(row=0, column=1)

def calculate_sum():
    n = int(n_entry.get())
    total = sum(range(1, n+1))

    # Hiển thị kết quả
    result_label.config(text=f"Tổng các số từ 1 đến {n} là {total}")

# Tạo một nút tính toán để tính tổng các số từ 1 đến N
    calculate_button = tk.Button(window, text="Tính tổng", command=calculate_sum)
    calculate_button.grid(row=1, column=0)

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.grid(row=1, column=1)
window.mainloop()