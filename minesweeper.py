def minesweeper(arr):
    # checking argument == list 
    if isinstance (arr, list):
        # new list to hold the values 
        result = [[0 for x in range(len(arr[0]))] for _ in range(len(arr))]
        # actual logic
        for rid,row in enumerate(arr):
            for cid,col in enumerate(row):
                # !mine
                if col == "-":
                    # !FIRST_COLUMN
                    if cid > 0:
                        # check WEST
                        if arr[rid][cid-1] == "#":
                            result[rid][cid]+=1
                        # check NORTH_WEST
                        if rid > 0 and arr[rid-1][cid-1]=="#":
                            result[rid][cid]+=1
                        # check SOUTH_WEST
                        if rid < len(arr)-1 and arr[rid+1][cid-1]=="#":
                            result[rid][cid]+=1
                    # !LAST_COLUMN
                    if cid < len(arr[0])-1:
                        # check EAST
                        if arr[rid][cid+1] == "#":
                            result[rid][cid]+=1
                        # check NORTH_EAST
                        if rid > 0 and arr[rid-1][cid+1] == "#":
                            result[rid][cid]+=1
                        # check SOUTH_EAST
                        if rid < len(arr)-1 and arr[rid+1][cid+1] == "#":
                            result[rid][cid]+=1
                    if rid > 0 and arr[rid-1][cid] == "#":
                        result[rid][cid]+=1
                    if rid < len(arr)-1 and arr[rid+1][cid] == "#":
                        result[rid][cid]+=1
                else:
                    result[rid][cid] = "#"
        return result
    else:
        print("The function only takes a list ")

                            

user_input = [["-","-","-","#","#"],
["-","#","-","-","-"],
["-","-","#","-","-"],
["-","#","#","-","-"],
["-","-","-","-","-"]]

print(minesweeper(user_input))