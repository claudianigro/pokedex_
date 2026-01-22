from django.http import JsonResponse
from .models import Pokemon
import json
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db import OperationalError, IntegrityError
@require_GET
def get_pokemon_list(request):
    try:
        pokemon_list = Pokemon.objects.all().values()
        return JsonResponse(list(pokemon_list), safe = False)
    except OperationalError:
        return JsonResponse({'error' : 'Database non disponibile'}, status = 503)
    except Exception as e:
        return JsonResponse({'error':str(e)}, status = 500)


@csrf_exempt
@require_POST
def add_pokemon(request):
    try:
        data = json.loads(request.body)
        pokemon = Pokemon.objects.create(name = data["name"], pokedex_id=data['pokedex_id'])
        return JsonResponse({'id': pokemon.id, 'name' : pokemon.name, 'pokedex_id':pokemon.pokedex_id }, status = 201)
    except IntegrityError:
        return JsonResponse("Errore! Pokemon già esistente. ")


@require_http_methods(['DELETE'])
def delete_pokemon(request,id):
    try:
        pokemon = Pokemon.objects.get(id=id)
        pokemon.delete
        return JsonResponse({'message':'Pokemon eliminato'}, status = 200)
    except:
        return JsonResponse({"Erroreeee"}, status =  404)
    
@csrf_exempt
@require_http_methods(['PATCH'])
def update_patch_pokemon(request, id):
    try:
        data = json.loads(request.body)
        pokemon = Pokemon.objects.get(id=id)

        if 'name' in data:
            pokemon.name = data['name']
        pokemon.save()

        return JsonResponse({
            'id': pokemon.id,
            'name' : pokemon.name,
            'pokedex_id': pokemon.pokedex_id
        }, status = 200)
    except Pokemon.DoesNotExist:
        return JsonResponse({'errore: Pokemon non trovato'}, status = 404)
    except json.JSONDecodeError:
        return JsonResponse({'error: JSON non valido'}, status = 400)
    

@csrf_exempt
@require_http_methods(['PUT'])
def update_put_pokemon(request, id):
    try:
        data = json.loads(request.body)
        pokemon = Pokemon.objects.get(id=id)
        pokemon.name = data['name']
        pokemon.pokedex_id = data['pokedex_id']
        pokemon.save()
        
        return JsonResponse({
            'id': pokemon.id,
            'name' : pokemon.name,
            'pokedex_id': pokemon.pokedex_id
        }, status = 200)
    except Pokemon.DoesNotExist:
        return JsonResponse({'errore: Pokemon non trovato'}, status = 404)
    except json.JSONDecodeError:
        return JsonResponse({'error: JSON non valido'}, status = 400)


