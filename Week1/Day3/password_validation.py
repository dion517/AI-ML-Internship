while True:
    password = input("Enter Password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters.")
        continue

    upper = False
    lower = False
    digit = False

    for ch in password:
        if ch >= 'A' and ch<= 'Z':
            upper = True
        elif ch >= 'a' and ch<= 'z':
            lower = True
        elif ch >='0' and ch<= '9':
            digit = True
        
        
       ## if ch.isupper():
         ##   upper = True
        ##elif ch.islower():
          ##  lower = True
        ##elif ch.isdigit():
          ##  digit = True



    if not upper:
        print("Password must contain at least one uppercase letter.")
        continue
    elif not lower:
        print("Password must contain at least one lowercase letter.")
        continue
    elif not digit:
        print("Password must contain at least one digit.")
        continue
    else:
        print("Password Accepted.")
        break 