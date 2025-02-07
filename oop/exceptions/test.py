ln = [2, 4, 5, 7]
n = input()

try:
    print(ln[int(n)])
except IndexError:
    print('n is larger than ln size.')
except ValueError as e:
    print(e)
