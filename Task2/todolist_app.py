n=1
def add(n):
    tempList=[]
    while True:
        str=input("Enter your task one by one(press end to exit):")
        tempList.append(str+'\n')
        if str in 'end':
            break
    tempList.pop()
    ft=open(r"to-doList.txt",'w')
    print("\n########## Your TODO List ##########",file=ft)
    print("------------------------------------",file=ft)
    fd=open(r"to-doList.txt",'a')
    for i in tempList:
        fd.write(f'{n}.'+i)
        n+=1
    return None

def remove():
    templst=[]
    removeId=input("Enter the task Id to remove from the todolist:")
    fd=open("to-doList.txt",'r')
    templst=fd.readlines()
    for i in range(3,len(templst)-1):
         if templst[i].startswith(removeId):
                   del templst[i]
                   break
    fw=open(r"to-doList.txt",'w')
    newlst=[]
    newlst.append(templst[0])
    newlst.append(templst[1])
    newlst.append(templst[2])
    k=1
    for i in range(3,len(templst)):
        newlst.append(f'{k}.'+templst[i][templst[i].index('.')+1:])
        k+=1
    for i in newlst:
            fw.write(i)
    exit()
  
def exit():
      return None

def view():
    fd=open(r"to-doList.txt",'r')
    lst=fd.readlines()
    for i in lst:
        print(i)
    return None


def main():
    while True:
        print("\n**************TO-DO List Manager**************")
        print("1.ADD\n2.REMOVE\n3.VIEW\n4.EXIT")
        choice=int(input("Enter your choice:"))
        if choice==1:
            add(n)
        if choice==2:
            remove()
        if choice==3:
            view()
        if choice==4:
            break
        


if __name__=="__main__":
    main()
