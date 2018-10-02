
while True:
    num = input ("Pleas enter digest: ")
    if num.isdigit():
        j = 1
        for f in range(1,int(num)+1):
            j *= f
        print("Factorial of %s is %d" % (num,j))
        break
