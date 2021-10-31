# multiple_test.py

print("Enter sufix:")
suffix = input()

print(f'suffix: {suffix}')

if suffix == '.htm':
    content = 'text/html'
elif suffix == '.jpg':
    content = 'image/jpeg'
elif suffix == '.png':
    cotent = 'image/png'
else:
    raise RuntimeError(f'Unknown content type {suffix!r}')


# Conditional expression

a = 25
b =  30

maxvalue = a if a > b else b

print(f'max value is {maxvalue}')

