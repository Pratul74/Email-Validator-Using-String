email=input("Enter Your Email: ")
ns=0
nc=0
nch=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]=='.') ^ (email[-3]=='.'):
                for ch in email:
                    if ch.isspace():
                        ns=1  
                    elif ch.isalpha():
                        if ch.isupper():
                            nc=1
                    elif ch.isdigit():
                        continue
                    elif ch=='_' or ch=='.' or ch=='@':
                        continue
                    else:
                        nch=1
                if ns or nc or nch:
                    print("Invalid Email!!")
                else:
                    print("Valid Email, Email approved")

            else:
                print("Invalid Email!!")
        else:
            print("Invalid Email!!")
    else:
        print("Invalid Email!!")
else:
    print("Invalid Email!!")