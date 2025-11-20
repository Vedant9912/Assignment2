# Name: Vedant Wagadre
# Enrollment: 0103AL231225
# Batch: 5
# Batch Time: 10:30

logged_user = ''
logged = False


dictfile={}
def register():
    global dictfile
    print("\n--- New User Registration ---")
    Userid = input("1. Enter the User ID (Username): ")
    
    if Userid in dictfile.keys():
        print('❌ User ID already taken. Please try again.')
        return

    #Password
    password = input("2. Create Password: ")

    details = {}
    details['Password'] = password
    details['Name'] = input("3. Enter Full Name: ")
    details['Email'] = input("4. Enter Email Address: ")
    details['Phone'] = input("5. Enter Phone Number: ")
    details['College_ID'] = input("6. Enter College ID/Roll No: ")
    details['Branch'] = input("7. Enter Branch: ")
    details['City'] = input("8. Enter City: ")
    details['Pincode'] = input("9. Enter Pincode: ")
    details['DOB'] = input("10. Enter Date of Birth (DD-MM-YYYY): ")
    dictfile[Userid] = details
    
    print("\n✅ Registration successful! Your data is:")
    print(f"User ID: {Userid}, Name: {details['Name']}, Email: {details['Email']}")

def login():
    global logged_user
    global logged
    global dictfile
    if logged:
        print(f" You are already logged in as **{logged_user}**.")
        return
    
    Userid = input("Enter your user ID: ")
    password = input("Enter your password: ")
    if Userid in dictfile:
        if dictfile[Userid]["Password"] == password:
            logged_user = Userid
            logged = True
            print(f" Login successful! Welcome back, **{logged_user}**!")
        else:
            print("❌ Login failed: Incorrect password.")
    else:
        print("❌ Login failed: User ID not found. Please register first.")

    pass

def show_profile():
    global logged_user
    global logged
    if logged:
        user_data = dictfile[logged_user]
        print("👤 User Profile")
        print(f"Logged in User ID: **{logged_user}**")
        print(f"Name: {user_data['Name']}")
        print(f"Email: {user_data['Email']}")
        print(f"Phone: {user_data['Phone']}")
        print(f"College ID: {user_data['College_ID']}")
        print(f"Branch: {user_data['Branch']}")
        print(f"City: {user_data['City']}")
        print(f"Pincode: {user_data['Pincode']}")
        print(f"DOB: {user_data['DOB']}")
        print("Status: Logged In ✅")
    else:
        print("❌ You need to **log in** first to view your profile.")

def update_profile():
    global logged_user
    global logged
    global dictfile
    if not logged:
        print("❌ You need to **log in** first to update your profile.")
        return
    profile=dictfile[logged_user]
    while True:
        print("\nUpdate options:")
        print("1 - Update fields (Name, Email, Phone, Branch, etc.)")
        print("2 - Change password")
        print("3 - Back to main menu")
        choice = input("Choose 1/2/3: ").strip()

        if choice == "1":
            print("\n--- Update Fields (Leave blank to keep current value) ---")
            
            # Name
            new_name = input(f"Full Name (Current: {profile['Name']}): ").strip()
            if new_name != "":
                profile['Name'] = new_name
            
            # Email
            new_email = input(f"Email (Current: {profile['Email']}): ").strip()
            if new_email != "":
                profile['Email'] = new_email

            # Phone
            new_phone = input(f"Phone (Current: {profile['Phone']}): ").strip()
            if new_phone != "":
                profile['Phone'] = new_phone

            # College_ID
            new_id = input(f"College ID/Roll No (Current: {profile['College_ID']}): ").strip()
            if new_id != "":
                profile['College_ID'] = new_id

            # Branch
            new_branch = input(f"Branch (Current: {profile['Branch']}): ").strip()
            if new_branch != "":
                profile['Branch'] = new_branch
            
            # City
            new_city = input(f"City (Current: {profile['City']}): ").strip()
            if new_city != "":
                profile['City'] = new_city
            # Pincode
            new_pincode = input(f"Pincode (Current: {profile['Pincode']}): ").strip()
            if new_pincode != "":
                profile['Pincode'] = new_pincode
            
            # DOB
            new_dob = input(f"DOB (DD-MM-YYYY) (Current: {profile['DOB']}): ").strip()
            if new_dob != "":
                profile['DOB'] = new_dob
            
            print("\n✅ Profile fields updated successfully!")
        elif choice == "2":
            print("\n--- Change Password ---")
            old_password = input("Enter your current password for verification: ").strip()
            if profile["Password"] == old_password:
                new_password = input("Enter the new password: ").strip()
                confirm_password = input("Confirm the new password: ").strip()
                if not new_password:
                    print("❌ New password cannot be empty.")
                elif new_password != confirm_password:
                    print("❌ Confirmation password is not matching.")
                else:
                    profile["Password"] = new_password
                    print("✅ Password updated successfully!")
            else:
                print("❌ Verification failed: Incorrect current password.")
        elif choice == "3":
            print(" Going back to main menu...")
            break 
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

def logout():
    global logged
    global logged_user
    logged=False
    logged_user=None
    print("Logout Successfully")

def terminate():
    print("Thank you for using LNCT system. Exiting...")
    exit()


def main():
    while True:
        print("Welcome in LNCT")
        response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit.

            select option 1/2/3/4/5/6/7: ''')
        if response == '1':
            register()
        elif response == '2':
            login()
        elif response == '3':
            show_profile()
        elif response == '4':
            update_profile()
        elif response == '5':
            logout()
        elif response == '6':
            main()
        elif response == '7':
            terminate()
        else:
            print("Invalid Choice, Please select correct option")
            continue
main()