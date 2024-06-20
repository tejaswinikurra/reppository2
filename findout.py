list = {23, 34, 56, 67, 89}
print(list)
target = int(input("enter the number"))


def linear(list, target):
    for i in range(len(list)):
        if target == list[i]:
            return 1
        else:
            return -1


result = linear(list, target)
if result != -1:
    print("found")
else:
    print("not found")
