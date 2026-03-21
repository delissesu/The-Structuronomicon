# Update
# Update the set by adding elements from an iterable/another set.
H = set("Hacker")
R = set("Rank")

H.update(R)
print(H)

# Intersection Update
# Update the set by keeping only the elements found in it and an iterable/another set.
A = set("Hacker")
B = set("Rank")

A.intersection_update(B)
print(A)

# Difference Update
# Update the set by removing elements found in an iterable/another set.
F = set("Hacker")
G = set("Rank")

F.difference_update(G)
print(F)

# Symmetric Difference
# Update the set by only keeping the elements found in either set, but not in both.
K = set("Hacker")
L = set("Rank")

K.symmetric_difference_update(L)
print(K)

# count = int(input())
# numbers = set(map(int, input().split()))
# third_number = int(input())

# for _ in range(third_number):
#     operation, _ = input().split()
#     other_set = set(map(int, input().split()))
#     if operation == "intersection_update":
#         numbers.intersection_update(other_set)
#     elif operation == "update":
#         numbers.update(other_set)
#     elif operation == "symmetric_difference_update":
#         numbers.symmetric_difference_update(other_set)
#     elif operation == "difference_update":
#         numbers.difference_update(other_set)

# print(sum(numbers))

def process_set_operations():
    # Dictionary mapping operation names to set methods
    operations = {
        'intersection_update': set.intersection_update,
        'update': set.update,
        'symmetric_difference_update': set.symmetric_difference_update,
        'difference_update': set.difference_update
    }
    
    # Get initial set
    n = int(input())
    main_set = set(map(int, input().split()))
    
    # Process operations
    for _ in range(int(input())):
        operation, _ = input().split()
        other_set = set(map(int, input().split()))
        
        # Get the corresponding method and apply it
        set_operation = operations.get(operation)
        if set_operation:
            set_operation(main_set, other_set)
    
    return sum(main_set)

if __name__ == "__main__":
    print(process_set_operations())