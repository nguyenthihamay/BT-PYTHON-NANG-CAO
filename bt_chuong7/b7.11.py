import tkinter as tk
from PIL import Image, ImageTk

# Hàm tính toán năm âm lịch Việt Nam
def am_lich(nam_duong):
    can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    nam_am_lich = can[nam_duong % 10] + " " + chi[nam_duong % 12]

    image_path = f"{chi[nam_duong % 12]}.jpg"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    return nam_am_lich, photo

# Hàm xử lý sự kiện khi nhấn nút chuyển đổi
def convert():
    nam_duong = int(year_entry.get())
    nam_am_lich, photo = am_lich(nam_duong)

    result_label.config(text=f"Năm âm lịch tương ứng là {nam_am_lich}")
    image_label.config(image=photo)
    image_label.image = photo

# Tạo một cửa sổ
window = tk.Tk()
window.title("Chuyển đổi năm Dương lịch sang năm âm lịch")

window.geometry("400x300")
tk.Label(window, text="Nhập năm Dương lịch:").grid(row=0, column=0)

year_entry = tk.Entry(window, width=30)
year_entry.grid(row=0, column=1)
convert_button = tk.Button(window, text="Chuyển đổi", command=convert)
convert_button.grid(row=1, column=0)

result_label = tk.Label(window, text="")
result_label.grid(row=1, column=1)

image_label = tk.Label(window)
image_label.grid(row=2, column=0, columnspan=2)

window.mainloop()