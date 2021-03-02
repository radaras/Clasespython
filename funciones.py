def clasificador_edades(edad):
    result=""
    if  edad  > 0 and edad <=5  :
        result="infante"
    if  edad  > 5 and edad <=13  :
        result="niño"
    if edad > 14 and edad <= 20:
        result = "adolecente"

    if edad > 20 and edad <= 45:
            result = "adulto"
    if edad > 45 and edad <= 100:
        result = "anciano"

    return result

print(clasificador_edades(60))