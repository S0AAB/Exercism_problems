def annotate(minefield:list):
    if not minefield:
        return []
    
    salida=[]
    filas= len(minefield)
    columnas=len(minefield[0])

  
    # Validar que todas las filas tengan el mismo número de columnas
    if any(len(fila) != columnas for fila in minefield):
        raise ValueError("The board is invalid with current input.")
    


    for i in range(0,filas):
      
      nuevaLinea=""
      for j in range (0,columnas):
         #Veriricar valores validos del tablero
         if (minefield[i][j] not in (" ", "*")):
             raise ValueError("The board is invalid with current input.")
         
         mineCount=0
         if(minefield[i][j]==" "):
            
            #Verificar bordes arriba
            if(i-1>=0):
                if(minefield[i-1][j]=="*"): #Mirar arriba
                    mineCount+=1
                if(j+1<columnas):
                     if(minefield[i-1][j+1]=="*"): #Mirar arriba derecha
                        mineCount+=1
                if(j-1>=0):
                     if(minefield[i-1][j-1]=="*"): #Mirar arriba izquierda
                        mineCount+=1
                
            #Verificar bordes izquierda
            if(j-1>=0):
                 if(minefield[i][j-1]=="*"): #Mirar izquierda
                   mineCount+=1
             
             #Verificar borders derecha
            if(j+1<columnas):
                 if(minefield[i][j+1]=="*"): #Mirar derecha
                   mineCount+=1


               #Verificar bordes inferiores
            if(i+1<filas):
                if(minefield[i+1][j]=="*"): #Mirar abajo
                    mineCount+=1
                if(j+1<columnas):
                    if(minefield[i+1][j+1]=="*"):#Mirar abajo derecha
                        mineCount+=1
                if(j-1>=0):
                    if(minefield[i+1][j-1]=="*"):#Mirar abajo derecha
                        mineCount+=1
               
        
            if(mineCount!=0):
                nuevaLinea+=str(mineCount)
            else:
                nuevaLinea+=" "
         else:
            nuevaLinea+="*"
      salida.append(nuevaLinea)
     
         
            
    return salida



