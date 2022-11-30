import requests
import json
import config
from config import new_pet, base_url, users_list
import datetime

# PETS
# POST/ Add a new pet to the store
pet = new_pet
pet['name'] = 'Rex'
pet['category']['name'] = 'Animal'
pet['tags'][0]['name'] = 'Dog'
pet['status'] = 'available'

header = {'accept': 'application/json',
          'Content-Type': 'application/json'}

res = requests.post(f'{base_url}/pet',
                    data=json.dumps(pet),
                    headers=header)

print('POST/ Add a new pet to the store')
print('Response status code:', res.status_code)
print(f'Server response body:\n{res.json()}')
print(f'Server response headers:\n{res.headers}\n')

updated_pet = res.json()
pet_id = res.json()["id"]

# POST/ Uploads an image
image = 'dog01.jpg'
content = {'file': (image, open(image, 'rb'), 'image/jpg')}
res = requests.post(f'{base_url}/pet/{pet_id}/uploadImage',
                          headers={'accept': 'application/json'},
                          files=content)

print('UPLOAD an IMAGE')
print('Response status code:', res.status_code)
print(f'Server response body:\n{res.json()}')
print(f'Server response headers:\n{res.headers}\n')

# PUT/ Update an existing pet
# updated_pet = res.json()
updated_pet['name'] = 'Чебурашка'
updated_pet['category']['name'] = 'Кеша'
updated_pet['tags'][0]['name'] = 'Собака'
updated_pet['status'] = 'sold'

header = {'accept': 'application/json',
          'Content-Type': 'application/json'}
res = requests.put(f'{base_url}/pet',
                     data=json.dumps(updated_pet).encode('utf-8'),
                     headers=header)

print('UPDATE a pet')
print('Response status code:', res.status_code)
print(f'Server response body:\n{res.json()}')
print(f'Server response headers:\n{res.headers}\n')

# GET/ Find a pet by ID
header = {'accept': 'application/json'}
res = requests.get(f'{base_url}/pet/{pet_id}', headers=header)

print('GET/pet  Find a pet by ID')
print('Response status code: ', res.status_code)
print(f'Server response body:\n{res.json()}')
print(f'Server response headers:\n{res.headers}\n')

# UPDATE pet with FORM DATA
header = {'accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded'}
name = 'Felix4444'
status = 'test_status'
form_data = f'name={name}&status={status}'
res = requests.post(f'{base_url}/pet/{pet_id}',
                         headers=header, data=form_data)

print('UPDATE pet with FORM DATA')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# GET/ Find Pets by status
statuses = ['pending', 'test_status']  #, 'placed']  # , 'available']
header = {'accept': 'application/json'}

for status in statuses:
    res = requests.get(f'{base_url}/pet/findByStatus?status={status}',
                       headers=header)

    print(f'\nFIND pets by STATUS "{status}"')
    print('Response status code:', res.status_code)
    print('Response body:')
    for _ in res.json():
        print(f'{_}')

    print('Response headers:\n', res.headers, '\n')

# DELETE A PET
header = {'accept': 'application/json'}
res = requests.delete(f'{base_url}/pet/{pet_id}',
                      headers=header)

print('DELETE /pet{petId}')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# PLACE AN ORDER
header = {'accept': 'application/json',
          'Content-Type': 'application/json'}
time = datetime.datetime.today()
order = config.order
order['petId'] = pet_id
order['shipDate'] = time.isoformat()
order = json.dumps(order, ensure_ascii=False)
res = requests.post(f'{base_url}/store/order',
                    headers=header,
                    data=order)
print('Place an order')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

order_ID = res.json()['id']

# FIND PURCHASE ORDER BY ID
header = {'accept': 'application/json'}
res = requests.get(f'{base_url}/store/order/{order_ID}', headers=header)
print('Find purchase order by ID')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# RETURN PET INVENTORIES BY STATUS
res = requests.get(f'{base_url}/store/inventory', headers=header)
print('Return pet inventories by status')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# DELETE ORDER
res = requests.delete(f'{base_url}/store/order/{order_ID}',
                      headers=header)

print('Delete Order')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')


#  Create a list of users with given input array
header = {'accept': 'application/json', 'Content-Type': 'application/json'}
list_of_users = json.dumps(users_list, ensure_ascii=False)

res = requests.post(f'{base_url}/user/createWithArray', headers=header, data=list_of_users)

print('CREATE A LIST OF USERS WITH GIVEN INPUT ARRAY')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# Create a list of users with given input list
res = requests.post(f'{base_url}/user/createWithList', headers=header, data=list_of_users)

print('CREATE A LIST OF USERS WITH GIVEN INPUT LIST')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# Create new user
new_user = json.dumps(config.user_frame, ensure_ascii=False)

res = requests.post(f'{base_url}/user', headers=header,  data=new_user)
print('CREATE A NEW USER')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# Get user by username
username = config.user_frame['username']
res = requests.get(f'{base_url}/user/{username}',
                   headers={'accept': 'application/json'})
print('GET USER BY USERNAME')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# Log user into system
password = config.user_frame['password']
header = {'accept': 'application/json'}
res = requests.get(f'{base_url}/user/login?username={username}&password={password}',
                   headers=header)
print('LOG USER INTO SYSTEM')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# Update user
header = {'accept': 'application/json', 'Content-Type': 'application/json'}
updated_user = json.dumps(config.updated_user, ensure_ascii=False)

res = requests.put(f'{base_url}/user/{username}', headers=header, data=updated_user)
print('UPDATED USER')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# Delete user
res = requests.delete(f'{base_url}/user/{username}', headers=header)
print('DELETED USER')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# Delete user

res = requests.delete(f'{base_url}/user/{config.updated_user["username"]}', headers=header)
print('DELETED USER')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())
print('Response headers:\n', res.headers, '\n')

# Log user out of system
res = requests.get(f'{base_url}/user/logout', headers={'accept': 'application/json'})
print('Logs user into system')
print('Response status code:', res.status_code)
print('Response body:\n', res.json())