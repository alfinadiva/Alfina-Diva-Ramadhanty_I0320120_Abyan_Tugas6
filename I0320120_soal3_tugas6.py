# menentukan suatu bilangan prima di rentang angka tertentu
for a in range(10, 25):
    for x in range(2, a):
        if (a % x) == 0:
            print("%d bukan prima" % a)
            break
    else:
        print("%d adalah bilangan prima" % a)