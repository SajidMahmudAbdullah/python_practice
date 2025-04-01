username_password = {"Sajid_Mahmud": "Saj123", "Sami_Mahfuz": "Sam123", "Sarah_Fatima": "Sar123"} 
first_name_last_name = {"Sajid Mahmud": "Abdullah", "Sami Mahfuz": "Abdullah", "Sarah": "Fatima"}
bank_info = {"Sajid Mahmud": 350, "Sami Mahfuz": 900, "Sarah Fatima": 566}
    
print(" _____ WELCOME TO THE BANK _____")

global username # A global variable can be accessed and modified from anywhere in the program

def login_function(): # contains all bank functions
    logged_in = False
    while not logged_in:
        global username
        username = input(" ENTER USERNAME : ")
        if username not in username_password:
            print(" USERNAME DOES NOT EXIST")
        else:
            password = input(" ENTER PASSWORD : ")          
            while password != username_password[username]:
                print(" INCORRECT PASSWORD")
                password = input(" ENTER PASSWORD : ")                
            logged_in = True
                               
def bank_function():
    while True:
        bank_options = input("\n BALANCE | DIPOSIT | WITHDRAW | LOGOUT [1|2|3|Q] : ")
        if options not in ("1", "2", "3"):
            print( " INVALID OPTION")
        else:
            if bank_options == "1":
                print(f" YOUR CURRENT BALANCE IS ${bank_info[username]}")
            elif bank_options == "2":
                deposit_amount = input(f" ENTER DEPOSIT AMOUNT : $")
                
                while True:  
                    try:
                        if deposit_amount.lower() == "q":
                            break
                        else:
                            deposit_amount = float(deposit_amount)
                            break          
                    except ValueError:
                        print(" INVALID INPUT")
                        deposit_amount = input(" ENTER DEPOSIT AMOUNT : $")
                bank_info[username] += deposit_amount
                print(f" CURRENT BALANCE ${bank_info[username]}")
            elif bank_options == "3":
                withdraw_amount = input(" ENTER WITHDRAW AMOUNT : $")
                while True:  
                    try:
                        if withdraw_amount.lower() == "q":
                            break
                        else:
                            withdraw_amount = float(withdraw_amount)
                            if withdraw_amount > bank_info[username]:
                                print(" WITHDRAW AMOUNT CAN NOT BE GREATER THAN YOUR BALANCE")
                                withdraw_amount = input(" ENTER WITHDRAW AMOUNT : $")
                                if withdraw_amount.lower() == "q":
                                    break                              
                            else:
                                print(" WITHDRAWL SUCCESSFUL")
                                bank_info[username] -= withdraw_amount
                                print(f" CURRENT BALANCE ${bank_info[username]}")
                                break
                    except ValueError:
                        print(" INVALID INPUT")
                        withdraw_amount = input(" ENTER WITHDRAW AMOUNT : $")            
            else:
                if bank_options.lower() == "q":
                    break
                else:
                    print(" INVALID INPUT")

while True:  
    options = input("\n LOGIN | REGISTER | DELETE ACCOUNT [1|2|3] : ")      
    if options not in ("1", "2", "3"):
        print( " INVALID OPTION")     
    else:
        if options == "1":        
            login_function()
            print(f" WELCOME {username}")
            bank_function()          
        elif options == "2":
            first_name = input(" ENTER FIRST NAME : ")
            last_name = input(" ENTER LAST NAME: ")
            
            
            new_username = input(" ENTER NEW USERNAME : ")
            while True:
                if len(new_username) > 15 and " " in new_username:
                    print(" USERNAME CAN NOT BE LONGER THAN FIFTEEN CHARACTERS ")
                    print(" USERNAME CAN NOT CONTAIN ANY SPACES ")
                    new_username = input(" ENTER NEW USERNAME : ")
                elif len(new_username) > 15:
                    print(" USERNAME CAN NOT BE LONGER THAN FIFTEEN CHARACTERS ")
                    new_username = input(" ENTER NEW USERNAME : ")
                elif " " in new_username:
                    print(" USERNAME CAN NOT CONTAIN ANY SPACES ")
                    new_username = input(" ENTER NEW USERNAME : ")
                else:
                    break
            while new_username in username_password:
                print(" USERNAME ALREADY EXISTS")
                new_username = input(" ENTER NEW USERNAME : ")        
            new_password = input(" ENTER NEW PASSWORD [ATLEAST 6 CHARACTERS] : ")
            while True:
                if len(new_password) < 6 and new_password == new_username and " " in new_password:
                    print(" PASSWORD CAN NOT BE THE SAME AS USERNAME")
                    print(" PASSWORD NEEDS TO BE ATLEAST SIX CHARACTERS LONG")
                    print(" PASSWORD CAN NOT CONTAIN ANY SPACES" )
                    new_password = input(" ENTER NEW PASSWORD : ")
                elif len(new_password) < 6 and new_password == new_username:
                    print(" PASSWORD CAN NOT BE THE SAME AS USERNAME")
                    print(" PASSWORD NEEDS TO BE ATLEAST SIX CHARACTERS LONG")
                    new_password = input(" ENTER NEW PASSWORD : ")
                elif new_password == new_username and " " in new_password:
                    print(" PASSWORD NEEDS TO BE ATLEAST SIX CHARACTERS LONG")
                    print(" PASSWORD CAN NOT CONTAIN ANY SPACES" )
                    new_password = input(" ENTER NEW PASSWORD : ")
                elif len(new_password) < 6 and " " in new_password:
                    print(" PASSWORD CAN NOT BE THE SAME AS USERNAME")
                    print(" PASSWORD CAN NOT CONTAIN ANY SPACES" )
                    new_password = input(" ENTER NEW PASSWORD : ")
                elif new_password == new_username:
                    print(" PASSWORD CAN NOT BE THE SAME AS USERNAME")
                    new_password = input(" ENTER NEW PASSWORD : ")
                elif len(new_password) < 6:
                    print(" PASSWORD NEEDS TO BE ATLEAST SIX CHARACTERS LONG")
                    new_password = input(" ENTER NEW PASSWORD : ")
                elif " " in new_password:
                    print(" PASSWORD CAN NOT CONTAIN ANY SPACES")
                    new_password = input(" ENTER NEW PASSWORD : ")             
                else:
                    break          
            username_password[new_username] = new_password       
            print(f" MINIMUM STARTING DEPOSIT $50")
            deposit = input(" DEPOSIT AMOUNT : $")
            while True:
                try:
                    if deposit.lower() == "q":
                        break
                    else:
                        deposit = float(deposit)
                        if deposit < 50:
                            print(" MINIMUM DEPOSIT AMOUNT $50")
                            deposit = input(" DEPOSIT AMOUNT : $")
                            if deposit.lower() == "q":
                                break
                        else:
                            bank_info[new_username] = deposit  
                            username = new_username
                            break
                except ValueError:
                    print( " INVALID INPUT")
                    deposit = input(" DEPOSIT AMOUNT : $")   
            print(f" WELCOME TO THE BANK {username}")
            bank_function()                    
        else: 
            login_function()
            del username_password[username]
            del bank_info[username]
            print(" YOUR ACCOUNT HAS BEEN DELETED")
            
