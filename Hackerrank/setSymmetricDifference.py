num_counter1 = int(input())
s1 = set(map(int, input().split()))

num_counter2 = int(input())
s2 = set(map(int, input().split()))

print(len(s1.symmetric_difference(s2)))
