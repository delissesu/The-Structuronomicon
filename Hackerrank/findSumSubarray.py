"""
Cari masing-masing elemen yang menghasilkan sebuah nilai target yang sudah ditentukan di sebuah list angka atau sama
dengan elemen itu sendiri jika sama dengan target.
Buat beberapa versi, baik naive (iteratif) atau menggunakan pointer.

Contoh:
List Angka = [1,8, 6, 9, 3, 10, 1]
Target = 9
Output = [1, 8], [6, 3], [9]
"""

# Naive Version (Brute Force)
def findSumSubarrayNaive(nums: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []
    n: int = len(nums)
    
    """
    1, 8, 2
    0
    0 stop sampai ke n elemen
    1 -> cursum
    8 -> cursum
    cursum == target -> 9
    
    result = []
    nums[0:2] -> slicing, itu stoppnya exclude
    misal [1, 2, 3] -> slicingnya [0:3]
    
    disini, yang direturn adalah 9
    
    """
    
    # Check all possible subarrays
    for i in range(n):
        current_sum: int = 0
        for j in range(i, n):
            current_sum += nums[j]
            
            if current_sum == target:
                result.append(nums[i:j+1])
            elif current_sum > target:
                break  # No need to continue if sum exceeds target
    
    return result


# Two Pointer Version (Optimized for positive numbers)
def findSumSubarrayTwoPointer(nums: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []
    n: int = len(nums)
    
    for start in range(n):
        left: int = start
        right: int = start
        current_sum: int = 0
        
        while right < n:
            current_sum += nums[right]
            
            # If sum equals target, add subarray to result
            if current_sum == target:
                result.append(nums[left:right+1])
                break
            # If sum exceeds target, break (for positive numbers only)
            elif current_sum > target:
                break
            
            right += 1
    
    return result


# Sliding Window Version (Most optimized for positive numbers)
def findSumSubarraySlidingWindow(nums: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []
    n: int = len(nums)
    
    # Start from each position
    for start in range(n):
        left: int = start
        right: int = start
        current_sum: int = 0
        
        while right < n:
            current_sum += nums[right]
            
            # If sum equals target, add subarray to result
            if current_sum == target:
                result.append(nums[left:right+1])
                break
            # If sum exceeds target, break
            elif current_sum > target:
                break
            
            right += 1
    
    return result


# Test the functions
def testAllVersions():
    test_nums: list[int] = [1, 8, 6, 9, 3, 10, 1]
    target_num: int = 9
    
    print("Input:", test_nums)
    print("Target:", target_num)
    print()
    
    print("=== CONTIGUOUS SUBARRAYS ===")
    print("Naive Version:")
    result_naive: list[list[int]] = findSumSubarrayNaive(test_nums, target_num)
    for idx, subarray in enumerate(result_naive):
        print(idx, subarray)
    print()
    
    print("Two Pointer Version:")
    result_two_pointer: list[list[int]] = findSumSubarrayTwoPointer(test_nums, target_num)
    for subarray in result_two_pointer:
        print(subarray)
    print()
    
    print("Sliding Window Version:")
    result_sliding: list[list[int]] = findSumSubarraySlidingWindow(test_nums, target_num)
    for subarray in result_sliding:
        print(subarray)
    print()
    
    print("=== ALL COMBINATIONS (Non-contiguous) ===")
    result_combinations: list[list[int]] = findSumCombinations(test_nums, target_num)
    for combination in result_combinations:
        print(combination)


# Bonus: Find all combinations that sum to target (not necessarily contiguous)
def findSumCombinations(nums: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []
    
    def backtrack(start: int, current_combination: list[int], current_sum: int):
        if current_sum == target:
            result.append(current_combination[:])  # Copy the current combination
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(nums)):
            current_combination.append(nums[i])
            backtrack(i + 1, current_combination, current_sum + nums[i])
            current_combination.pop()  # Backtrack
    
    backtrack(0, [], 0)
    return result


# Run test
testAllVersions()