import requests
parameters = {
    "amount": 10,
    "type": "boolean"
}
data = requests.get('https://opentdb.com/api.php', params=parameters)

question_data = data.json()['results']
