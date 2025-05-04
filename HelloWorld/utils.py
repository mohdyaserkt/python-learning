def find__max(numbers):
    maxNumber=numbers[0]
    for number in numbers:
        if number>maxNumber:
            maxNumber=number
    print(f'greatest number is {maxNumber}')


