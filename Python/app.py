import math

def solution(k: int) -> int:
    if k == 1:
        return 0

    nums = [1]
    current_sum = 1
    operations = 0

    while current_sum < k:
        if current_sum * 2 <= k:
            duplicate_ops = 1  # 1 operation for duplication
            duplicated_nums = nums + nums
            duplicated_sum = current_sum * 2

            remaining = k - duplicated_sum
            if remaining > 0:
              duplicated_nums.sort()
              i = 0
              while remaining > 0:
                duplicated_nums[i] +=1
                remaining -=1
                duplicate_ops +=1
                i = (i+1)%len(duplicated_nums)

            increment_ops = 0
            temp_nums = nums[:] #create a copy
            temp_sum = current_sum
            remaining_increment = k - current_sum
            temp_nums.sort()
            i = 0
            while remaining_increment>0:
                temp_nums[i] +=1
                remaining_increment -= 1
                increment_ops+=1
                i = (i+1)%len(temp_nums)

            if duplicate_ops <= increment_ops:
                nums = duplicated_nums
                current_sum *= 2
                operations += 1
            else:
                min_index = nums.index(min(nums))
                nums[min_index] += 1
                current_sum += 1
                operations += 1
        else:
            min_index = nums.index(min(nums))
            nums[min_index] += 1
            current_sum += 1
            operations += 1

    return operations

# Custom Test Cases
print(min_operations(15))  # Output: 6
print(min_operations(3))   # Output: 2
print(min_operations(1))   # Output: 0
print(min_operations(10))  # Output: 5
print(min_operations(20))  # Output: 7
print(min_operations(100)) # Output: 14