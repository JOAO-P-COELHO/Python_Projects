import requests # Importar um package (neste caso o package para pudermos fazer um API request)

while True:
    pokemon = input("Write the name of a pokemon: (control+C para sair)")
    pokemon = pokemon.lower()
    source = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    require_dadosAPI = requests.get(source)


    if require_dadosAPI.status_code==200:
        dados = require_dadosAPI.json()
        dados_habilidade = dados["abilities"]
        
        for habilidades in dados_habilidade:
            print (f"O nome da habilidade é:\t{habilidades["ability"]["name"]}")

    else:
        print ("Esse pokemon não existe")