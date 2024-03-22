from providers.response import healthcheck_response


def test_healthcheck_response():
    assert healthcheck_response.exec({}).get("healthcheck") == True
