def sum_to(n):
    a=0
    for i in range(n):
        a += (i+1)
    return a

while True:
    sequence = int(input("Import Sequence?: "))
    print(sum_to(sequence))
    
