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

list3 = list1 + list2
final_list = list(set(list3))
print("Union of entered two lists = ",final_list)
