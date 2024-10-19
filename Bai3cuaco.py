import math # bài 56 ko dùng chữ nhật
def chuvi_dt(*args, hinh, pheptinh):
    
    if hinh == 'vuong':
        canh = args[0]
        return 4*canh if pheptinh == 'chuvi' else canh**2
    #if pheptinh == "chuvi:"
    #   return 4*canh
    #else:
    #   return canh**2
    
   # elif hinh == "chunhat":
        #dai = args[0]
        #rong = args[1]
        #return 2*(dai+rong) if pheptinh == "chuvi" else dai*rong
    elif hinh == "tron":
        bk = args[0]
        return 2*math.pi*bk if pheptinh == "chuvi" else math.pi*bk
    else:
        return "hinh khong hop le"
    
if __name__=="__main__":
    print("chu vi hinh vuong:", chuvi_dt(3,hinh='vuong',pheptinh='chuvi'))
    print("dien tich hinh vuong:", chuvi_dt(3,hinh='vuong',pheptinh='dientich'))
   # print("chu vi hinh chu nhat:", chuvi_dt(3,4,hinh='chunhat',pheptinh='chuvi'))
  
   # print("dien tich hinh chu nhat:", chuvi_dt(3,4,hinh='chunhat',pheptinh='dientich'))
    print("chu vi hinh tron:", chuvi_dt(3,hinh='tron',pheptinh='chuvi'))
    print("dien tich hinh tron:", chuvi_dt(3,hinh='tron',pheptinh='dientich'))    