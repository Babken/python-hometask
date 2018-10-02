while True:
    password = input ("Password Validator: ")
    cl = False
    cu = False
    for i in password:
        if i.isdigit():
            cl = True
        elif i.isupper():
            cu = True

        if cl == True and cu == True:
            break

    if cl == True and cu == True:
        print(password)
        break
