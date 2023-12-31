import tkinter as tk
window = tk.Tk()
window.title("Nhập thông tin sinh viên")
window.geometry("400x200")
# Tạo các hộp văn bản
ten_sv = tk.Entry(window, width=30)
id_sv = tk.Entry(window, width=30)
mat_khau = tk.Entry(window, width=30)
# Thiết lập vị trí của các hộp văn bản
ten_sv.grid(row=0, column=1)
id_sv.grid(row=1, column=1)
mat_khau.grid(row=2, column=1)
# Tạo các nhãn cho các hộp văn bản
tk.Label(window, text="Tên sinh viên:").grid(row=0, column=0)
tk.Label(window, text="ID sinh viên:").grid(row=1, column=0)
tk.Label(window, text="Mật khẩu:").grid(row=2, column=0)
gui_button = tk.Button(window, text="Gửi")
gui_button.grid(row=3, column=1)
window.mainloop()