def min(numbers):
    min = numbers[0]

    for num in numbers:
        if min > num:
            min = num

    return min

def max(numbers):
    max = numbers[0]

    for num in numbers:
        if max < num:
            max = num

    return max
