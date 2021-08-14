
import pymongo,re
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client['CollegeDb']
Collection_name =mydatabase['student']
studentlist=[]

def validate(r):
    reg=re.match("[0-9]",r)
    if (reg):
        return True
    else:
        return False

while True:
    print("\n1. Add Students")
    print("\n2. Search Students")
    print("\n3. Update Students")
    print("\n4. Delete Students")
    print("\n5. View Students count of each branch")
    print("\n6. View all Students")
    print("\n7. Exit")
    ch=int(input("Enter a choice"))

    if(ch == 1):
        name=input("Enter  name :")
        rollno=input("Enter  roll no :")
        branch=input("Enter  branch :")
        mydict={"name":name,"rollno":rollno,"branch":branch,"del_status":0}
        if(validate(rollno)):

            studentlist.append(mydict)
            Collection_name.insert_many(studentlist)
            studentlist.clear()
        else:
            print("Invalid Roll no")
    
    if (ch == 2):
        name = input("\n Enter name ?")
        result=Collection_name.find({"name":name,"del_status":0})
        for i in result:
            print(i)
    if(ch == 4):
        rollno = input("Enter the roll no to be DELETED ?")
        Collection_name.update_one({"rollno":rollno},{"$set":{"del_status":1}})

    if (ch == 5):
        result=Collection_name.aggregate([{"$group": {"_id":"$branch","no_of_students":{"$sum": 1}}}])
        for i in result:
            print(i)

    if (ch == 6):
        break


