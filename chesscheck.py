def safe_pawns(pawns):
    count = 0
    # print(sorted(pawns))
    pawns_indexes = set()
    for p in sorted(pawns):
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row,col))
    print(pawns_indexes)
    for row,col in pawns_indexes:
        is_safe = ((row - 1, col -1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
        if is_safe:
            count += 1
    return count


#sorted = ['b4', 'c3', 'd2', 'd4', 'e3', 'f4', 'g5']
ans = safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) #6
print(ans)
