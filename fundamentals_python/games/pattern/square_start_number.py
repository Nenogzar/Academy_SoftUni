# row = 5
# for count in range(1, row*5+1):
#     print(f"{('*' if count %2 else count//2):>3}", end='' if count % 5 else '\n')


j, k = 0, 1
while j < 25:
    for column in range(5):
        if j % 2 == 0:
            print(f"{"*":<3}", end="")
        else:
            print(f"{k:<3}", end ='')
            k+=1
        j+=1
    print()