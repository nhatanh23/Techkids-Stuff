
a =["bra", "panties"," male panties"]
while True:

    
    n = input("Welcome, What do you want?(C, R, U, D,S)")
    print (n)
    if n == "c" or n == "C":
        new_item = input("New item?")
        a.append(new_item)
        for j in (a):
            print (j,',',end='')
        print()
    elif n == "r" or n =="R":
        for i in (a):
            print (i,',', end='')
        print()
    elif n == "u" or n =="U":
        pos = int(input("Update position? "))
        new_item = input("New item?" )
        a[pos]= new_item
        print("Our updated items: ", end= '')
        for i in range(len(a)-1):
            print(a[i], end=', ')
        print(a[len(a)-1])
        print()
    elif n == "d" or n =="D":
        pos = int(input("Delete position? "))
        if pos < len(a):
            a.pop(pos)
            print("Our updated items:", end='')
            for i in range(len(a)-1):
                print(a[i], end=',')
            print(a[len(a)-1])
        else:
            print("try again")
