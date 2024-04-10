from providers.response import healthcheck_response


def test_healthcheck_response():
    assert healthcheck_response.exec({}).get("healthcheck") == True


def test_healthcheck_response_error():
    response = healthcheck_response.exec({"errors": [{"step1": None}]})
    assert response != {"healthcheck": True}
