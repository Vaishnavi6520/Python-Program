import re,sys,csv
from datetime import datetime
import time
try:
    header = ["productname","discription","price","manufacturer","manufacturingdate","expirydate","AddOn"]
    productlist=[]
    class ProductDetails:
        def addproductdetails(self,productname,discription,price,manufacturer,manufacturingdate,expirydate):
            current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
            dict1={"productname":productname,"discription":discription,"price":price,"manufacturer":manufacturer,"manufacturingdate":manufacturingdate,"expirydate":expirydate,'AddOn':current_time}
            productlist.append(dict1)
    obj1=ProductDetails()
    def val(price):
        v=re.search("^[1-9]",price)
        if v:
            return int(price)
    while(True):
        print("1.Add Products")
        print("2.View all products")
        print("3.Search a product")
        print("4.list all the products that expired today")
        print("5.For CSV file")
        print("6.exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            productname=input("enter the product name - ")
            discription=input("enter the description of product - ")
            price=input("enter the price - ")
            manufacturer=input("enter the manufacturer name - ")
            manufacturingdate=input("enter date in mm-dd-yyyy format -")
            expirydate=input("enter the expiry date in mm-dd-yyyy format - ")
            obj1.addproductdetails(productname,discription,val(price),manufacturer,manufacturingdate,expirydate)
        if choice==2:
            print(productlist)
        if choice==3:
            S=input("enter the product to search - ")
            r=productlist.find({"productlist":S})
            print(r)
        if choice==4:
            print("list all the products that expire today - ")
            current_date=time.strftime("%m-%d-%Y-",time.localtime())
            expired=(list(filter(lambda i:i["expirydate"]==str(current_date),productlist)))    
            if len(expired)>0:
                print(expired)
            else:
                print("No Expired product found")
        if choice == 5:
            with open('product.csv','w+',encoding='UTF8',newline='') as s:
                writer = csv.DictWriter(s,fieldnames=header)
                writer.writeheader()
                writer.writerows(productlist)
        if choice==6:
            sys.exit()
except Exception:
    print('something went wrong')
finally:
    print("Thank You!!")