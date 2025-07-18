def recite(start, take=1):
    salida=[]
    numbers=["no","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    verse1="green bottles hanging on the wall,"
    verse2="And if one green bottle should accidentally fall,"
    verse3="There'll be"
    final_verse="green bottles hanging on the wall."

    for i in range(take,0,-1):
        current_verse = verse1
        if(numbers[start] == "one"):
            current_verse = current_verse.replace("bottles", "bottle")
        salida.append(f"{numbers[start].capitalize()} {current_verse}")
        salida.append(f"{numbers[start].capitalize()} {current_verse}")
        salida.append(f"{verse2}")
        
        current_final = "green bottles hanging on the wall."
        if(numbers[start-1] == "one"):
            current_final = current_final.replace("bottles", "bottle")
        salida.append(f"{verse3} {numbers[start-1]} {current_final}")
        
        start-=1
        if(i > 1):  
            salida.append("")
    return salida 

print(recite(start=3,take=3))


