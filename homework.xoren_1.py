import sys

if len(sys.argv) < 2:
    print("Please pass command line arguments")

args = ' '.join(sys.argv[1:])
while len(args) != 0:
    for char in args:
         break
    print("occurrence of %s is %d" % (char,args.count(char)))
    args = args.replace(char, "")
