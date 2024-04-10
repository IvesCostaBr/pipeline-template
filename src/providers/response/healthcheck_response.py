def exec(data):
    if data.get("errors"):
        return data.get("errors")
    return {"healthcheck": True}
