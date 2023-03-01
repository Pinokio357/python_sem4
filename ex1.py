leight_1 = int(input("enter first list count: "))
leight_2 = int(input("enter second list count: "))
list_1 = [int(input("enter element of first list: ")) for _ in range(leight_1)]
print("---------------------------------")
list_2 = [int(input("enter element of second list:")) for _ in range(leight_2)]
print(list_1)
print(list_2)
my_list = sorted(set(list_1 + list_2))
print("result list: ")
print(my_list)