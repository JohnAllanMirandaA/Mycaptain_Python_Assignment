num_list=input("Enter the number seperated with spaces:")
num_list=num_list.split()
num_list=[int(num) for num in num_list]
posnum=[]
for num in num_list:
    if num>0:
        posnum.append(num)
print("The positive numbers in the are :",posnum)

