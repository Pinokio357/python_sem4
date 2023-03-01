from random import randint
count_bush = int(input("enter bush count: "))
berrry_each_bash_list = [randint(100, 300) for _ in range(count_bush)]
print(berrry_each_bash_list)
max_berry_count = 0
new_list = berrry_each_bash_list*3
for bash in range(count_bush, count_bush*2):
    temp = new_list[bash] + new_list[bash - 1] + new_list[bash + 1]
    if temp > max_berry_count:
        max_berry_count = temp

print(f"max berry count = {max_berry_count}")