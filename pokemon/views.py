from django.http import JsonResponse
from .models import Pokemon

def pokemon_list(request):
    lista_pokemon = Pokemon.objects.all().values()
    print(lista_pokemon)
    return JsonResponse(list(lista_pokemon), safe = False)

def add_pokemon(request):
    pokemon = Pokemon.objects.create(nome = "Pokemon", tipo = "Fuoco", is_owned = False )
    return JsonResponse({'id': pokemon.id, 'nome' : pokemon.nome, 'tipo': pokemon.tipo, 'is_owned': pokemon.is_owned})