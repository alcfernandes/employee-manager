def get_token(client):
    token_response = client.post('/api/token/', {'username': 'user@test.com', 'password': 'TestPass#1970'})
    return token_response.data['access']
