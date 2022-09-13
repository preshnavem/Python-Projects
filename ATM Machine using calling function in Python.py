#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("!***Union Bank of India Welcomes You!***!")
pin_number = int(input("Enter ATM Pin Number: "))
Amount = 25000
if(pin_number == 1234):
    print("Enter 1: Withdraw\nEnter 2: Balance Enquiry\nEnter 3: Fast Transaction\n")
    a = int(input("Enter Option: "))
    def withdraw():
        w=int(input("Enter withdraw amount: "))
        if (w < Amount):
            print("Please collect your amount:", w)
            print("Thank You for Banking with us")
        else:
            print("Invalid cash")
    def Balance():
        print("Available Balance in your account is: ", Amount)
        print("Thank You for Banking with us\n")
        print("Do you want to Continue for withdraw?\n")
        yes = int(input("Press 1 if you want to continue:"))
        withdraw()
    def Fast():
        print("1: 1000\n2: 5000\n3: 10000\n4: 15000")
        b = int(input("Enter Fast Transaction Option:")) 
        trans = "1000" if (b == 1) else "5000" if (b == 2) else "10000" if (b == 3) else "15000" if ( b == 4) else print("Invalid Option Selected") 
        print("Please collect your cash:", trans)
    if(a==1):
        withdraw()
    elif(a==2):
        Balance()
    elif(a==3):
        Fast()
else:
    print("Invalied Pin Number")


# In[ ]:




