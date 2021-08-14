import pymongo

#1.Servername=>Localhost
#2.Database=> StudentDb
#3.Username =>
#4.Password =>


client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = client['StudentDb']
collection_name=mydatabase["students"]

getName=input("Enter a name : ")
getRoll=input("Enter a roll number : ")
getAdmin=input("Enter a admission number : ")
getCollege=input("Enter a College name : ")

data={"name":getName,"rollno":getRoll,"Admno":getAdmin,"college":getCollege}
print(data)
collection_name.insert_one(data)