def solution(A):
    digit_sums_map = {}

    for num in A:
        digit_sum_value = sum(int(digit) for digit in str(num))

        if digit_sum_value not in digit_sums_map:
            digit_sums_map[digit_sum_value] = [num]
        else:
            digit_sums_map[digit_sum_value].append(num)

    max_sum = -1

    for key in digit_sums_map:
        numbers = digit_sums_map[key]

        if len(numbers) >= 2:
            current_sum = sum(numbers)
            max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases
print(solution([51, 71, 17, 42])) 
print(solution([43, 9, 63])) 
print(solution([51, 32, 43]))
