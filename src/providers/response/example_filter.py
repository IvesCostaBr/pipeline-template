

def exec(data):
    response = data.get('filter_examples')
    if not response.get('status'):
        return {"error": data.get('errors')}
    
    return response.get('data')