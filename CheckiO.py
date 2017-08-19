def long_repeat(line):
    count = 1
    max = 1
    print(line)
    letter = ""
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            count += 1
            letter = line[i]
        if line[i] != line[i+1] and line[i] != letter:
            count = 1
        if max < count:
            max = count
    if line:
        return max
    else:
        return 0

print(long_repeat('ddvvrwwwrggg'))