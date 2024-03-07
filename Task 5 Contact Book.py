contact=[]
def addcontact():
    num=int(input("Enter the number of contacts you want to add:"))
    for i in range(num):
        name=input("Enter name:")
        phone_no=int(input("Enter the phone number:"))
        email_id=input("Enter the email id :")
        a=input("Enter the address:")
        m=[name,phone_no,email_id,a]
        contact.append(m)
        print("Contact Information saved Successfully!!")
        
def viewcontacts():
    print("The Contact Information is as follows: ")
    for i in contact:
        print(i)
    
def searchcontact():
    s=input("Enter the name to search:")
    f=0
    for i in contact:
        if i[0]==s:
            f=1
            print("The details are as follows: ")
            print(i)
    if f==0:
        print("No such Name Found")    
        
def deletecontact():
    t=input("Enter the name of the person whose contact you want to delete:")
    f=0
    for i in contact:
        if i[0]==t:
            f=1
            contact.remove(i)
            print("The contact of the given person has been deleted successfully")
    if f==0:
        print("No Such Name Found")
            
def updatecontact():
    t=input("Enter the Name of the person whose contact you want tp update: ")
    f=0
    for i in contact:
        if i[0]==t:
            f=1
            contact.remove(i)
            name=input("Enter name:")
            phone_no=int(input("Enter the phone number:"))
            email_id=input("Enter the email id :")
            a=input("Enter the address:")
            m=[name,phone_no,email_id,a]
            contact.append(m)
            print("Updated Successfully")
    if f==0:
        print("No Such Name Found")
                
while True:
    print("***** Welcome to Contact Book *****")
    print("1.ADD")
    print("2.VIEW")
    print("3.SEARCH")
    print("4.DELETE")
    print("5.UPDATE")
    print("6.EXIT")
    ch=int(input("Enter your choice from the following:"))
    if(ch==1):
        addcontact()
    elif(ch==2):
        viewcontacts()
    elif(ch==3):
        searchcontact()
    elif(ch==4):
        deletecontact()
    elif ch==5:
        updatecontact()
    elif(ch==6):
        print("Exiting the Menu")
        break
    else:
        print("Enter the correct choice!!")
