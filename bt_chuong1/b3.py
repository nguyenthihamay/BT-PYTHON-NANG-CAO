class phanso:
    def __init__(self,tu_so,mau_so):
        self.tu_so=tu_so
        self.mau_so=mau_so
    def kiem_tra_hop_le(self):
        return self.mau_so !=0
    def nhap_phan_so(self):
        self.tu_so=int(input("nhập tử số:"))
        self.mau_so=int(input("nhập mẫu số(khác 0):"))
    def in_phan_so(self):
        print(f"phân số:{self.tu_so}/{self.mau_so}")
#tạo một đối tượng phân số và nhập dữ liệu
ps=phanso(0,1)
ps.nhap_phan_so()
#kiểm tra tính hợp lệ của phân số 
if ps.kiem_tra_hop_le():
#in thông tin của phân số
   ps.in_phan_so()
else:
    print("phân số không hợp lệ!mẫu số phải khác 0")