str = input()
arr = []
for char in str:
    if (char == '='):
        if (len(arr) == 0):
            continue
        arr.pop()
    else:
        arr.append(char)
print(''.join(arr))