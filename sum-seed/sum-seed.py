number = 111

def sum_seed(number):
    for i in range(1, number + 1):
        newnum = i
        for d in str(i):
            newnum += int(d)
        if newnum == number:
            print(i)

sum_seed(number)
