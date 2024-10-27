def moore_automata(sequence):
    # Definimos el estado inicial
    state = 'S0'
    output = ''

    for char in sequence:
        if state == 'S0':
            if char == '0':
                output += '0'
                state = 'S0'
            elif char == '1':
                output += '1'
                state = 'S1'

        elif state == 'S1':
            if char == '0':
                output += '1'
                state = 'S0'
            elif char == '1':
                output += '0'  # Primer "0" de "00"
                state = 'S2'

        elif state == 'S2':
            output += '0'  # Segundo "0" de "00"
            state = 'S0'

    return output

# Prueba de la función con una secuencia
sequence = "110111011"
print("Entrada:", sequence)
print("Salida:", moore_automata(sequence))
