import re
def checkio(text):
    mvp = ''
    max = 1
    a = []
    b = []
    text = text.lower()
    for x in text:
        a.append(x)
    a.sort()
    for x in a:
        if x.islower() and not(x.isdigit()) and re.match('[a-zA-Z0-9]',x) \
                and not(re.match('-',x)):
            b.append(x)
            if max < text.count(x):
                max = text.count(x)
                mvp = x
            if max == 1:
                mvp = b[0]
    return mvp

ans = checkio("a-z")
print(ans)
