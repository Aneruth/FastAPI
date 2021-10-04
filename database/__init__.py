import asyncio
import aiomysql
import json
from fastapi import HTTPException
import os
import ssl

loop = asyncio.get_event_loop()

config = {'Username': 'root',
            'Password': 'root',
            'Host': 'localhost',
            'DB': 'users',
            'raise_on_warnings': True,
            'Port':3306}

# Encrypted connection using TLS/SSL: Flexible Server supports encrypted connections using Transport Layer Security (TLS 1.2)
# all incoming connections with TLS 1.0 and TLS 1.1 will be denied by default.
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)


async def execute(query, placeholder={}):
    try:
        conn = None
        conn = await aiomysql.connect(
            host=config["Host"],
            port=int(config["Port"]),
            user=config["Username"],
            password=config["Password"],
            db=config["DB"],
            cursorclass=aiomysql.cursors.DictCursor,
            autocommit=False,
            ssl=ctx,
        )

        async with conn.cursor() as cur:
            await cur.execute(query, placeholder)
            result = await cur.fetchall()
            print(cur._last_executed)  # need to log this
        await conn.commit()
        conn.close()
        return result
    except Exception as e:
        if conn:
            await conn.rollback()
            raise Exception(e)
        else:
            raise HTTPException(status_code=503, detail="Database Unreachable")
    finally:
        if conn:
            conn.close()


async def executemany(query, placeholder={}):
    try:
        conn = None
        conn = await aiomysql.connect(
            host=config["Host"],
            port=int(config["Port"]),
            user=config["Username"],
            password=config["Password"],
            db=config["DB"],
            cursorclass=aiomysql.cursors.DictCursor,
            autocommit=False,
            ssl=ctx,
        )

        async with conn.cursor() as cur:
            await cur.executemany(query, placeholder)
            result = await cur.fetchall()
            # print(cur._last_executed)  # need to log this
        await conn.commit()
        return result
    except Exception as e:
        if conn:
            await conn.rollback()
            raise Exception(e)
        else:
            raise HTTPException(status_code=503, detail="Database Unreachable")
    finally:
        if conn:
            conn.close()
