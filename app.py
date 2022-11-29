import requests
import json
from config import new_pet, base_url


def add_new_pet(pet):
    """POST /pet  Add a new pet to the store"""

    pet = new_pet
    pet['name'] = 'Rex'
    pet['category']['name'] = 'Animal'
    pet['tags'][0]['name'] = 'Dog'
    pet['status'] = 'available'

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res = requests.post(f'{base_url}/pet',
                             data=json.dumps(pet),
                             headers=header)

    return res.json(), res.status_code

# ADD a NEW PET
added_pet, added_pet_status_code = add_new_pet(new_pet)

# GET a PET
header = {'accept': 'application/json'}
res_get = requests.get(f'{base_url}/pet/{added_pet["id"]}', headers=header)

print ('POST /pet  Add a new pet to the store')
print ('Status code:', added_pet_status_code)
print(f'Server response body of the added pet in JSON-format:\n{res_get.json()}\n')
print(f'Server response headers of the added pet:\n{res_get.headers}\n')

# UPLOAD IMAGE
image = 'dog01.jpg'
content = {'file': (image, open(image, 'rb'), 'image/jpg')}
res_image = requests.post(f'{base_url}/pet/{added_pet["id"]}/uploadImage',
                          headers={'accept': 'application/json'},
                          files=content)

print('UPLOAD an IMAGE')
print('Status code:', res_image.status_code)
print('Response body:', res_image.json(), '\n')

# DELETE a PET
header = {'accept': 'application/json'}
res_delete = requests.delete((f'{base_url}/pet/{added_pet["id"]}'), headers=header)

print('DELETE /pet{petId}  Deletes a pet')
print(f'Status code after deleting: {res_delete.status_code}\n'
      f'Response body in JSON-format: ', res_delete.json())

