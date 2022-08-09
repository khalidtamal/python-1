num=int(input("Plz enter any num :"))
if num>0:
    print("The",num,"is positive")
elif num==0:
    print("The",num,"is Zero")
else:
    print("The",num,"is negative")

# same program just apply %d,%f placeholder
num=int(input("Plz enter any num :"))
if num>=0:
    print("%d is positive number"%(num))
else:
    print("%d is negative number"%(num))