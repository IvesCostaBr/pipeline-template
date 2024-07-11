

def exec(data):
    response = data.get('create_example')
    if not response.get('status'):
        return {"error": data.get('errors')}
    
    return response.get('data')