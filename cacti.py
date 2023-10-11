def cacti_number(array):
    
    row = len(array)
    column = len(array[0])
    count = 0

    for i in range(row):
        for k in range(column):
            
            if array[i][k] == 0 :
                canPlant = True
                if i>0 and array[i-1][k] == 1:
                    canPlant = False
                if k>0 and array[i][k-1] == 1:
                    canPlant = False
                if k < column - 1 and array[i][k+1] == 1:
                    canPlant = False
                if i < row - 1  and array[i+1][k] == 1:
                    canPlant = False
                    
                if canPlant:
                    array[i][k] = 1
                    count += 1
            
            
    return count

