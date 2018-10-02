while True:
    username = input ("Username: ")
    password = input ("Password: ")
    if username == 'Batman' and password == 'I am Batman':
        print("Welcome %s" % username)
        break
    else:
        print("Username or Password is incorrect\nPlease try again")
