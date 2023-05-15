import csv

def leer_pokemon_csv(file):
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        pokemons = []
        for row in reader:
            if row[0].isdigit() and row[1].isdigit() and row[2].isdigit():
                pokemons.append((int(row[0]), int(row[1]), int(row[2])))
    return pokemons

def algoritmo_voraz(pokemons):
    pokemons.sort(key=lambda x: (-x[2], x[1]))  # Ordenar por valor decreciente y luego por plazo creciente
    secuencia_captura = [[] for _ in range(len(pokemons))]
    dias_captura = [0] * (len(pokemons) + 1)

    for i in range(len(pokemons)):
        d = min(pokemons[i][1], len(pokemons))
        while d > 0 and dias_captura[d] != 0:
            d -= 1

        if d > 0:
            secuencia_captura[d - 1].append(pokemons[i])
            dias_captura[d] = 1

    return secuencia_captura

# Carga pokemons desde el archivo CSV
pokemons = leer_pokemon_csv('pokemon.csv')

# Aplica el algoritmo voraz
capturados = algoritmo_voraz(pokemons)

# Imprime los pokemons capturados
for i, pokemons_dia in enumerate(capturados):
    if len(pokemons_dia) > 0:
        print(f'Día {i + 1}:')
        for p in pokemons_dia:
            print(f'\tPokemon {p[0]}, Valor: {p[2]}, Plazo: {p[1]}')
