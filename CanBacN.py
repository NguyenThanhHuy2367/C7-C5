z=int(input("căn bậc = "))
m=int(input("Số = "))
h=int(input("Số chẵn âm = "))
a=int(input("Số kiểm tra = "))
def can_bac_n(x, n):
    return x ** (1/n)

a = can_bac_n(m, z)
print(f"căn bậc {z} của {m}= {a}")  


def binhphuong(n):
    if n>0:
        return n**2
    else:
        return "không hợp lệ"
print(f"Binh phương của {m} = ",binhphuong(m))


def sochanam(n):
    return n<0 and n%2==0
print("Số chẵn âm = ",sochanam(h))


def kiemtraso(n):
    if n<0 and n%2 != 0:
        return -1
    elif n>0 and n%2==0:
        return 1
    else :
        return 0
print(f"Kiểm tra số {a} = ",kiemtraso(a))


def kiemtragiatri():
    x=input("Kiểm tra giá trị nhập x =")

    if x.replace('.','',1).replace('-','',1).isdigit():
        x = float(x)
    if -89  <= x <= 90:
            return x 
    print("Không hợp lệ")
    return kiemtragiatri()

print("Kiểm tra giá trị  = ", kiemtragiatri())
        
