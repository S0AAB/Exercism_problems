def saddle_points(matrix):
    if not matrix:
        return []
        
    saddle_points = []
    rows = len(matrix)
    columns = len(matrix[0])

    try:
        for i in range(rows):
            for j in range(columns):
                # Obtener la columna j
                columna=[]
                for row in matrix:
                    columna.append(row[j])

                # Verificar si es el máximo en su fila y mínimo en su columna
                if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min(columna):
                    saddle_points.append({"row": i+1, "column": j+1})
    except:
       raise ValueError("irregular matrix")
    
    return saddle_points
