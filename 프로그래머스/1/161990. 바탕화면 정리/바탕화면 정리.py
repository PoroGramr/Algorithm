import copy

def solution(wallpaper):
    answer = []
    y = len(wallpaper)
    x = len(wallpaper[0])
    
    files = []
    
    
    for cy in range(0,y):
        for cx in range(0,x):
            if wallpaper[cy][cx] == "#":
                files.append([cy,cx])
    
    list_row = copy.deepcopy(files)
    list_col = copy.deepcopy(files)
    
    list_row.sort(key = lambda x : (x[0], x[1]))
    
    list_col.sort(key = lambda x : (x[1], x[0]))
    
    answer.append(list_row[0][0])
    answer.append(list_col[0][1])
    answer.append(list_row[-1][0] + 1)  
    answer.append(list_col[-1][1] + 1)  
    
    
    print(answer)
    return answer