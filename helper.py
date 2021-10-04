from fastapi import Form
from fastapi.responses import JSONResponse


def response_format(message="ok", code=200, ok=True, data=None, **others):
    return JSONResponse(
        content={
            "message": message,
            "code": code,
            "ok": ok,
            "data": data,
            **others,
        },
        status_code=code,
    )

def log(s):
    print(s)