def return_pipe(data):
    return [
        {
            "name": "filter_examples",
            "provider": "example",
            "module": "filter" 
        },
        {
            "name": "response",
            "provider": "response",
            "module": "example_filter"
        }
    ]
