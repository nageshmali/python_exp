list1 = []
list2 = []

print("Enter 5 elements in list1")
for i in range(0,5):
    ele = int(input("Enter element = "))
    list1.append(ele)

print("Enter 5 elements in list2")
for i in range(0,5):
    ele = int(input("Enter element = "))
    list2.append(ele)

final_list = [value for value in list1 if value in list2]
print("Intersection of entered two lists = ",final_list)