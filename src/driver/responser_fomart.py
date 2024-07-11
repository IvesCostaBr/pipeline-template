from fastapi.responses import JSONResponse

def fastapi_formatter(response, caseError: int):
    if type(response) == dict and response.get('error'):
        return JSONResponse({"error": response.get('error')}, status_code=caseError)
    if type(response) == list:
        return {"data": response}
    return response