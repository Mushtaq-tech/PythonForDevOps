mylist=[]
def totalNumber(count):
    for i in range(0,count):
        num=int(input("Enter numbers: "))
        mylist.append(num)

def calAverage():
    sum=0
    for i in range (0,len(mylist)):
        sum=sum+mylist[i]
    return (sum/count)


count=int(input("Avg of how many numbs?"))
totalNumber(count)

average=calAverage()
print("Total average is ", average)