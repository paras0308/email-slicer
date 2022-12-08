print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|       WELCOME TO EMAIL SLICER!!          |")
print("|        CREATED BY PARAS DHIMAN           |")
print("|    of Lovely Professional University     |")
print("|                                          |")
print("|                (•.•)/                    |")
print("|                <) )                      |")
print("|                 | |                      |")
print("|                                          |")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
while True:
    n=int(input("PRESS 1 TO FOR EMAIL SLICER"
                "          OR               "
                "     PRESS 2 TO EXIT       "))
    if n==1:
        def email_slicer(email):
            username, _, domain = email.strip().partition("@")
            return f"Your username is {username} & domain is {domain.upper()}"
        i=0
        while i==0:
            user_input = input("Enter Your Email: ")
            print(email_slicer(user_input))
            n=input("press \"yes\" to enter another email or press \"no\" to exit: ")
            if n=="yes":
                i=0
            else:
                i=1
    else:
        print("THANK YOU FOR USING EMAIL SLICER!!!")
        break
