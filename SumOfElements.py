lst = []
size = int(input("Enter the size of the list:"))

for i in range(size):
    ele = int(input("Enter an element in the list:"))
    lst.append(ele)

target = int(input("Enter the target number:"))
found = False  
for j in range(size):
    for k in range(j + 1, size):
        if lst[j] + lst[k] == target:
            found = True
            print(f"For the given target, your indexes are {j} and {k}")

if not found:
    print("No pairs found")

                
