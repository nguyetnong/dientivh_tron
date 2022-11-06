import tinhchuvi

dai=float(input("nhap chieu đai can tinh:"))
rong=float(input("nhap chieu rong can tinh:"))
bankinh=float(input("nhap ban kinh:"))
toado=float(input("nhap goc can tinh:"))
               
giatri = tinhchuvi.Tinh_Chu_Vi(chieudai = dai,chieurong = rong)
giatri2 = tinhchuvi.Tinh_Dien_tich(chieudai = dai,chieurong = rong)
print ("chu vi hcn cd {cd} va cr {cr} la:".format(cd=dai,cr=rong))
print ("dien tich hcn cd {cd} va cr {cr} la:".format(cd=dai,cr=rong))

tinhchuvi.hinhtron(r=bankinh)


tron=tinhchuvi.chuvi_hinhtron(r=bankinh,goc=toado)
tron2=tinhchuvi.tinhdientich(r=bankinh,goc=toado)

print("chu vi hinh tron ban kinh = {r} la {c}:".format(r=bankinh,c=tron))
print("dien tich tron ban kinh ={r} la {s}:".format(r=bankinh,s=tron2))