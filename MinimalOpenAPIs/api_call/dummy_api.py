import requests, json
from . import url


def keyData(comm_payload, response):
    try:
        post_iothub = url["DEMO"]["DEMO_DATA"]
        resp = requests.post(url=post_iothub, json=comm_payload)
        response.status_code = resp.status_code
        return resp
    except Exception:
        response.status_code = 500
        return {"Unsuccessful": "Server Is Not Responding"}