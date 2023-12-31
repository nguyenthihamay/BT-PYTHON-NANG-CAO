import math
class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Elip(Diem):
    def __init__(self, tam, a, b):
        super().__init__(tam.x, tam.y)
        self.a = a
        self.b = b
    def tinh_dien_tich(self):
        return math.pi * self.a * self.b
class DuongTron(Elip):
    def __init__(self, tam, r):
        super().__init__(tam, r, r)
tam = Diem(0, 0)
elip = Elip(tam, 3, 4)
print(elip.tinh_dien_tich())  
duong_tron = DuongTron(tam, 5)
print(duong_tron.tinh_dien_tich()) 