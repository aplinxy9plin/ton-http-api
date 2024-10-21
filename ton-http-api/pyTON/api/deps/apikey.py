from fastapi import Depends, Request, HTTPException
from fastapi.security.api_key import APIKeyHeader, APIKeyQuery

API_KEY_1 = "api_key_1"
API_KEY_2 = "api_key_2"

ALLOWED_IPS = [
    "65.109.0.107",
    "37.27.186.230",
    "37.27.25.147",
    "95.216.141.144",
    "95.216.142.30",
]

ALLOWED_ORIGINS = [
    "https://app.fomo.fund",
    "https://fomo.fund",
    "https://app-admin.fomo.fund"
]


def api_key_dep(request: Request,
                api_key_header: APIKeyHeader = Depends(APIKeyHeader(name='X-API-Key', auto_error=False)),
                api_key_query: APIKeyQuery = Depends(APIKeyQuery(name='api_key', auto_error=False))):
    client_ip = request.client.host
    origin = request.headers.get("Origin")

    if api_key_query == API_KEY_1:
        if client_ip not in ALLOWED_IPS:
            raise HTTPException(status_code=403, detail="Forbidden")
    elif api_key_query == API_KEY_2:
        if origin not in ALLOWED_ORIGINS:
            raise HTTPException(status_code=403, detail="Forbidden")
    else:
        raise HTTPException(status_code=403, detail="Forbidden")

    return api_key_query
