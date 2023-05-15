import pandas as pd

# Lee el dataset de Pokemon desde el archivo local
file_path = "pokemon.csv"
df = pd.read_csv(file_path)

# Extrae el valor y los días disponibles para cada Pokemon
pokemon_data = []
for index, row in df.iterrows():
    pokemon_data.append((row['name'], row['generation'], row['base_total']))

# Ordena la lista de Pokemon por generación y valor en orden descendente
sorted_pokemon = sorted(pokemon_data, key=lambda x: (-x[1], -x[2]))

# Algoritmo voraz para maximizar el valor total de los Pokemon capturados
days_left = len(set([p[1] for p in sorted_pokemon]))
captured_pokemon = []

for pokemon in sorted_pokemon:
    if days_left >= pokemon[1]:
        captured_pokemon.append(pokemon)
        days_left -= 1
    if days_left == 0:
        break

# Imprime la lista de Pokemon capturados y el valor total
captured_value = sum([p[2] for p in captured_pokemon])
print("Pokemon capturados:", [p[0] for p in captured_pokemon])
print("Valor total:", captured_value)