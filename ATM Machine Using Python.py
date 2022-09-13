#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Welcome Comment
print("!***Union Bank of India Welcomes You!***!")

#User Details
pin_number = int(input("Enter ATM Pin Number: "))
Amount = 25000

#Available ATM Options
if(pin_number == 1234):
    print("Enter 1: Withdraw\nEnter 2: Balance Enquiry\nEnter 3: Fast Transaction\n")
    a = int(input("Enter Option: "))
    #For Withdraws
    if (a == 1):
        w=int(input("Enter withdraw amount: "))
        if (w < Amount):
            print("Please collect your amount:", w)
            print("Thank You for Banking with us")
        else:
            print("Invalid cash")
    #For Balance Enquiry
    elif (a == 2):
        print("Available Balance in your account is: ", Amount)
        print("Thank You for Banking with us\n")
        print("Do you want to Continue?\n")
        
        #For Withdraw again
        yes = int(input("Press 1 if you want to continue"))
        if(yes ==1):
            if(pin_number == 1234):
                print("Enter 1: Withdraw\nEnter 2: Balance Enquiry\nEnter 3: Fast Transaction\n")
                a= int(input("Enter Option: "))
                if (a == 1):
                    w=int(input("Enter withdraw amount: "))
                    if (w < Amount):
                        print("Please collect your amount:", w)
                        print("Thank You for Banking with us")
                    else:
                        print("Invalid cash")
    #For Fast Transaction
    elif (a == 3):
        print("1: 1000\n2: 5000\n3: 10000\n4: 15000")
        b = int(input("Enter Fast Trasaction Option:"))
        if (b == 1):
            print("Please collect Amount: 1000")
            print("Thank You for Banking with us")
        elif (b == 2):
            print("Please collect Amount: 5000")
            print("Thank You for Banking with us")
        elif (b == 3):
            print("Please collect Amount: 10000")
            print("Thank You for Banking with us")
        elif (b == 4):
            print("Please collect Amount: 15000")
            print("Thank You for Banking with us")
        else:
            print("Invalid Option Selected")
    else:
        print("Invalid Option Selected")
else:
    print("Invalied Pin Number")


# In[ ]:




