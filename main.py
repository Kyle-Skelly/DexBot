# This is just a general helloworld style program using the pokeAPI
# that gives back the name of the pokemon requested by the user via commandline input

import requests
import json

requestedPokemon = input("Please enter the number of the pokemon you would like to learn more about: ")
resp = requests.get('http://pokeapi.co/api/v2/pokemon/' + requestedPokemon)
json_response = json.loads(resp.content)
print("Pokemon Name: " + json_response['name'])
