def checkio(game_result):
    g = game_result
    print(g)

    #X
    if (g[0][0] == g[0][1] == g[0][2] == "X") or \
        (g[0][0] == g[1][1] == g[2][2] == "X") or \
        (g[0][0] == g[1][0] == g[2][0] == "X") or \
        (g[0][2] == g[1][1] == g[2][0] == "X") or \
        (g[0][1] == g[1][1] == g[2][1] == "X") or \
        (g[0][2] == g[1][2] == g[2][2] == "X") or \
        (g[1][0] == g[1][1] == g[1][2] == "X") or \
        (g[2][0] == g[2][1] == g[2][2] == "X"):
            # print('winner X')
            return "X"
    #O
    elif (g[0][0] == g[0][1] == g[0][2] == "O") or \
        (g[0][0] == g[1][1] == g[2][2] == "O") or \
        (g[0][0] == g[1][0] == g[2][0] == "O") or \
        (g[0][2] == g[1][1] == g[2][0] == "O") or \
        (g[0][1] == g[1][1] == g[2][1] == "O") or \
        (g[0][2] == g[1][2] == g[2][2] == "O") or \
        (g[1][0] == g[1][1] == g[1][2] == "O") or \
        (g[2][0] == g[2][1] == g[2][2] == "O"):
            # print('winner O')
            return "O"
    else:
        # print("no winner")
        return "D"

    # return "D" or "X" or "O"



ans = checkio([
        "X.O",
        "XX.",
        "XOO"])
print(ans)
