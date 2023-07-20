

# User input example
# [["-","-","#","-","#"],
# ["-","-","#","-","#"],
# ["-","-","#","-","#"],
# ["-","-","#","-","#"],
# ["-","-","#","-","#"]]
user_input = [["-","-","-","#","#"],
["-","#","-","-","-"],
["-","-","#","-","-"],
["-","#","#","-","-"],
["-","-","-","-","-"]]

grid_size = len(user_input)
no_of_elements = grid_size**2 - 1


def question_print(x):
    for r in x:
        for c in r:
            print(c,end=",")
        print("")


question_print(user_input)


def get_bombs(row,col):
    no_of_bombs = 0
    # print(row)
    for r in range(max(0,row-1),min(grid_size-1,row+1)+1):
        for c in range(max(0,col-1),min(grid_size-1,col+1)+1):
            if r == row and c == col:
                continue
            if user_input[r][c] == "#":
                no_of_bombs+=1
    return no_of_bombs

def grid_board(x):
    for rid,r in enumerate(x):
        print("------------")
        for cid,c in enumerate(r):
            if x[rid][cid] is not "#":
                x[rid][cid] = get_bombs(rid,cid)
                print(x[rid][cid], end=",")
            else:
                x[rid][cid] = "#"
                print(x[rid][cid], end=",")
        print("")
        
grid_board(user_input)