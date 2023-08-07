def solution(wallpaper):
    row_size = len(wallpaper)
    column_size = len(wallpaper[0])
    min_lx = 50
    min_ly = 50
    max_rx = 0
    max_ry = 0
    
    
    for i in range(row_size):
        for j in range(column_size):
            if wallpaper[i][j] == '#':
                if i < min_lx:
                    min_lx = i
                if i < min_ly:
                    min_ly = j
                if i < min_lx:
                    max_rx = i
                if i < min_lx:
                    max_ry = j
                # if i + j > max_idx[0] + max_idx[1]:
                #     max_idx[0], max_idx[1] = i, j 
    
    
                
        
    answer = [min_lx, min_ly, max_rx + 1, max_ry + 1]
    return answer