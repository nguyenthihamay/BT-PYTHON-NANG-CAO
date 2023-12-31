import tkinter as tk
window = tk.Tk()
window.title("Nhập tên và tuổi của bạn")
window.geometry("400x200")

tk.Label(window, text="Nhập tên của bạn:").grid(row=0, column=0)

name_entry = tk.Entry(window, width=30)
name_entry.grid(row=0, column=1)

tk.Label(window, text="Nhập tuổi của bạn:").grid(row=1, column=0)

# Tạo một hộp văn bản để người dùng nhập tuổi
age_entry = tk.Entry(window, width=30)
age_entry.grid(row=1, column=1)
def process_info():
    name = name_entry.get()
    age = int(age_entry.get())
    if age >= 18:
        message = "Bạn đã trưởng thành!"
    else:
        message = "Bạn còn nhỏ tuổi!"
        result_label.config(text=f"Xin chào {name}.\n{message}")

# Tạo một nút để xử lý thông tin người dùng
process_button = tk.Button(window, text="Xử lý thông tin", command=process_info)
process_button.grid(row=2, column=0)

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=1)
window.mainloop()