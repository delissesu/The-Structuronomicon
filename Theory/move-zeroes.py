# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# number = [0, 1, 0, 3, 12]
number = list(map(int, input().strip().split()))
# temp = []
# temp_number = []

# for i in range(len(number)):
#     # print(i)
#     if number[i] == 0:
#         temp.append(0)

# for j in range(len(number)):
#     if number[j] > 0:
#         temp_number.append(number[j])
    
# number.clear()
# # print(number)
# # print(temp);print(temp_number)
# number = temp_number + temp
# print(number)

index = 0
# Good solution
for i in range(len(number)):
    if number[i] != 0:
        number[index] = number[i]
        index += 1

for j in range(index, len(number)):
    number[j] = 0

print(number)

# Another solution
snowball_size = 0

for i in range(len(number)):
    if number[i] == 0:
        snowball_size += 1
    elif snowball_size > 0:
        temp = number[i]
        number[i] = 0
        number[i - snowball_size] = temp
print(number)