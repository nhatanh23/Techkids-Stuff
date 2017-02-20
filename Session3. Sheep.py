sheep = [ 2, 23, 45, 56, 345, 67, 78,123]
print ("Hi my name is NA and these are my sheep sizes")
print (sheep)
n = 5
for i in range (1, n):
    print ("Now my biggest sheep has size", max(sheep), "let shear it")

    sheep[sheep.index(max(sheep))] = 8
    print ("After shearing, here is my flock")
    print(sheep)

    print("month", i,':')
    for j in range(len(sheep)):
        sheep[j-1] = int(sheep[j-1])+50
    print("One month has passed, now here is my flock:")
    print (sheep)
print()

total = sum(sheep)
print ("My flock has size in total", total)
print('I would get',total,'* $2 = $',total*2)
