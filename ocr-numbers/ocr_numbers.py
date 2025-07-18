def convert(input_grid):
    
    if(len(input_grid)%4!=0):
        raise ValueError ("Number of input lines is not a multiple of four")
    for fila in input_grid:
        if(len(fila)%3!=0):
            raise ValueError ("Number of input columns is not a multiple of three")

    numbers=""

    for numberY in divideY(input_grid):
        for numero in divide(numberY):
            numbers+=getUniqueNumber(numero)
        numbers+=","
    
    numbers=numbers[0:-1]
    return numbers
   

def divideY(input):
    salida=[]
    times=len(input)//4
    multi=0
    for u in range (0,times):
        salida2=[]
        for i in range (0,4):
            linea=""
            for j in range(0,len(input[0])):
                linea+=input[i+multi][j]
            salida2.append(linea)
        salida.append(salida2)
        multi+=4
    return salida


def divide(input):
    salida=[]
    times=len(input[0])//3
    multi=0
    for u in range (0,times):
        salida2=[]
        
        for i in range (0,4):
            linea=""
            for j in range(0,3):
                linea+=input[i][j+multi]
            salida2.append(linea)
        salida.append(salida2)
        multi+=3

    return salida
          

def getUniqueNumber(input):
        numbers = [
            [" _ ", "| |", "|_|", "   "],  # 0
            ["   ", "  |", "  |", "   "],  # 1
            [" _ ", " _|", "|_ ", "   "],  # 2
            [" _ ", " _|", " _|", "   "],  # 3
            ["   ", "|_|", "  |", "   "],  # 4
            [" _ ", "|_ ", " _|", "   "],  # 5
            [" _ ", "|_ ", "|_|", "   "],  # 6
            [" _ ", "  |", "  |", "   "],  # 7
            [" _ ", "|_|", "|_|", "   "],  # 8
            [" _ ", "|_|", " _|", "   "]   # 9
        ]
        salida=""

        for i in range(0,len(numbers)):

            if(input==numbers[i]):
                return str(i)
        return "?"   


