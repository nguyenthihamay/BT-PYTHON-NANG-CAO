class TS:
    def __init__(self,ho_ten,diem_toan,diem_ly,diem_hoa):
        self.ho_ten=ho_ten
        self.diem_toan=diem_toan
        self.diem_ly=diem_ly
        self.diem_hoa=diem_toan
    def nhap_thong_tin(self):
        self.ho_ten = input("nhập họ tên thí sinh:")
        self.diem_toan=float(input("nhập điểm toán:"))
        self.diem_ly=float(input("nhập điểm lý:"))
        self.diem_hoa=float(input("nhập điểm hóa:"))
    def tinh_tong_diem(self):
        return self.diem_toan+self.diem_ly+self.diem_hoa
    def in_thong_tin(self):
        print(f"họ tên thí sinh:{self.ho_ten}\n","tổng điểm:",self.tinh_tong_diem())
#--------------------------------------
n=int(input("nhập số lượng thí sinh:"))
ds_thi_sinh=[]
for i in range(n):
    ts=TS("",0,0,0)
    ds_thi_sinh.append(ts)
    ts.nhap_thong_tin()
#----------------------------------------
print("danh sách thí sinh trúng tuyển:")
ds_trung_tuyen=[]
for ts in ds_thi_sinh:
    if ts.tinh_tong_diem()>=20:
        ds_trung_tuyen.append(ts)
ds_trung_tuyen.sort(key=lambda ts:ts.tinh_tong_diem(),reverse=True)
#------------------------------------------
for ts in ds_trung_tuyen:
    ts.in_thong_tin()
