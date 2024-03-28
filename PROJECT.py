import requests

def fetch_pokemon_details(pokemon_name):
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        
        pokemon_data = response.json()
        
        # Print out the pokemon details
        print("\n~~~~~~~Pokemon Details~~~~~~~")
        print("\nName\t\t\t",pokemon_data['name'].upper())
        print("\nAbilities:")
        for ability in pokemon_data['abilities']:
            print(f"\t- {ability['ability']['name']}")
   
    else:
        print(f"Failed to fetch Pokemon details for '{pokemon_name}'.")


pokemon_name = input("Enter the name of the Pokemon you want to search: ").lower()
    
fetch_pokemon_details(pokemon_name)
