import requests

resp = requests.get('https://jsonplaceholder.typicode.com/posts')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /todos/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['title']))