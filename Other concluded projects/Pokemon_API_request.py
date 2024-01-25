import requests # Importar um package (neste caso o package para podermos fazer um API request)

while True: # Isto faz com que o programa nunca pare de pedir um input
    pokemon = input("\nWrite the name of a pokemon: [Control+C to leave]  ") # Pede o input ao user
    pokemon = pokemon.lower() # Como as strings são imutáveis, é necessário atribuir novamente a variável, ainda que com o mesmo nome
    source = f"https://pokeapi.co/api/v2/pokemon/{pokemon}" # Cria-se uma nova string em que parte do URL é dinâmico (depende do Input)

    require_dadosAPI = requests.get(source) # Faz-se o request API ao servidor desse url (que depende da source) e ele devolve o código na página

    if require_dadosAPI.status_code==200: # Se o site existir, ou seja, há um pokemon com esse nome, então a página tem de devolver .status_code==200
        dados = require_dadosAPI.json() # Como o pokemon/site existem, os dados/o código nesse site existente são convertidos em JSON (formato legível)
        dados_habilidade = dados["abilities"] # Aqui é feito um apanhado ao objeto dentro da list, é aqui que estão os dados que eu decidi querer
        
        for habilidades in dados_habilidade: # Como o pokemon tem várias habilidades, eu quero imprimir o nome de cada uma dessas habilidades
            print (f"The pokemon has this hability:\t{habilidades["ability"]["name"]}") 

    else:
        print ("Esse pokemon não existe") # Se o pokemon não existir (ou o site), este no site aparece como "Not found", e o .status_code=/=200,
        # logo, esta condição é ativada