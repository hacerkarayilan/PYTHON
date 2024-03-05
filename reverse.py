def reverse(numbers):
    numbers = [11, 42, -5, 27, 0, 89]
    for i in range(0, len(numbers) // 2):
        temp = numbers[i]
        numbers[i] = numbers[len(numbers) - 1 - i]
        numbers[len(numbers) - 1 - i] = temp
    print(numbers)
reverse(numbers)
