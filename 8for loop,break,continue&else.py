for i in range(1, 11):
    if i == 3:
        break
    print(i)
#or
    if i == 4 or i == 5 or i == 6:
        continue
    print(i)
    #or
    for i in range(1,11):
        if i==45:
            break
        print(i)
    else:
            print("no break was encontered")