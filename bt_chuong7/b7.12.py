import tkinter as tk
window = tk.Tk()
window.title("Tính chỉ số BMI")
window.geometry("400x200")

# Tạo một nhãn để yêu cầu người dùng nhập cân nặng
tk.Label(window, text="Nhập cân nặng của bạn (kg):").grid(row=0, column=0)

weight_entry = tk.Entry(window, width=30)
weight_entry.grid(row=0, column=1)

# Tạo một nhãn để yêu cầu người dùng nhập chiều cao
tk.Label(window, text="Nhập chiều cao của bạn (m):").grid(row=1, column=0)

# Tạo một hộp văn bản để người dùng nhập chiều cao
height_entry = tk.Entry(window, width=30)
height_entry.grid(row=1, column=1)

def calculate_bmi():
    # Lấy giá trị của cân nặng và chiều cao từ hộp văn bản
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    # Tính chỉ số BMI
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        message = "Bạn gầy!"
    elif bmi < 25:
        message = "Bạn bình thường."
    elif bmi < 30:
        message = "Bạn thừa cân."
    else:
        message = "Bạn béo phì!"
    result_label.config(text=f"Chỉ số BMI của bạn là {bmi:.1f}.\n{message}")
# Tạo một nút tính toán để tính chỉ số BMI và hiển thị kết quả
calculate_button = tk.Button(window, text="Tính chỉ số BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0)

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=1)

# Hiển thị cửa sổ
window.mainloop()


