def return_pipe(data):
    return [
        {
            "name": "filter_examples",
            "provider": "example",
            "module": "filter" 
        },
        {
            "name": "job",
            "provider": "example",
            "module": "job",
            "condition": data.get('limit'),
            "async": True 
        },
        {
            "name": "response",
            "provider": "response",
            "module": "example_filter"
        }
    ]
