s =  tuple()
m =  int(input("enter how many elements you want :"))
for i in range(0,m):
    num = int(input("enter number:"))
    s = s + (num, )
print("The numbers in tuple are: \n", s)
