from ...api_call.dummy_api import keyData


# This function will generate the token.
def dummy_control(dummy_payload, key, response):
    resp = keyData(dummy_payload, key)
    if resp.status_code==200:
        response.status_code = resp.status_code
        return resp.json()
    else:
        response.status_code = resp.status_code
        return resp.json()