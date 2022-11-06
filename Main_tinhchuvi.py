import tinhchuvi

dai=float(input("nhap chieu đai can tinh:"))
rong=float(input("nhap chieu rong can tinh:"))
bankinh=float(input("nhap ban kinh:"))
toado=float(input("nhap goc can tinh:"))
               
giatri = tinhchuvi.Tinh_Chu_Vi(chieudai = dai,chieurong = rong)
giatri2 = tinhchuvi.Tinh_Dien_tich(chieudai = dai,chieurong = rong)
print (giatri)
print (giatri2)

tinhchuvi.hinhtron(r=bankinh)


tron=tinhchuvi.chuvi_hinhtron(r=bankinh,goc=toado)
tron2=tinhchuvi.tinhdientich(r=bankinh,goc=toado)

print(tron)
print(tron2)