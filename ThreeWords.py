def checkio(words):
    new = words.split()
    print(new)
    count = 0
    for word in new:
        if word.isalpha():
            count += 1
            if count >= 3: break
        if word.isdigit():
            count = 0
        print(count)
    if count >= 3:
        return True
    else:
        return False

print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))