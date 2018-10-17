text = input()

try:

    number = int(text)
    print(number + 1)

except ValueError:
    print('thats not a number')
