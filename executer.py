import database
from fastapi import HTTPException

async def create_user(data):
    try:
        query = open("./query/create_user.sql",
            "r",
        ).read()
        # Stores the result from the query in a variable and returns the data
        result = await database.execute(query, data)
        return result
    except Exception as e:
        if type(e) is HTTPException:
            raise HTTPException(status_code=e.status_code,
                                detail=str(e.detail))
        raise HTTPException(status_code=500, detail=str(e))

async def create_address(data):
    try:
        query = open("./query/create_address.sql",
            "r",
        ).read()
        result = await database.execute(query, data)
        return result
    except Exception as e:
        if type(e) is HTTPException:
            raise HTTPException(status_code=e.status_code,
                                detail=str(e.detail))
        raise HTTPException(status_code=500, detail=str(e))

async def get_users():
    try:
        query = open("./query/get_users.sql",
            "r",
        ).read()
        result = await database.execute(query)
        return result
    except Exception as e:
        if type(e) is HTTPException:
            raise HTTPException(status_code=e.status_code,
                                detail=str(e.detail))
        raise HTTPException(status_code=500, detail=str(e))

async def delete_user(data):
    try:
        query = open("./query/delete_user.sql",
            "r",
        ).read()
        result = await database.execute(query, data)
        return result
    except Exception as e:
        if type(e) is HTTPException:
            raise HTTPException(status_code=e.status_code,
                                detail=str(e.detail))
        raise HTTPException(status_code=500, detail=str(e))

async def update_user(data):
    try:
        query = open("./query/update_user.sql",
            "r",
        ).read()
        s = ''
        # print(data)
        for i in data:
            # print(i,type(data[i]),data[i])
            ''' if we provide only one input and if rest of the input is None and it considers 
            the valued input alone'''
            if data[i] != None:
                s+= i+'=%('+i+')s'+','
        # replace the given input in the query and executes query in line number 76
        query = query.format(s[:-1])
        # print("\n\n\nQuery",query,'\n\n')
        result = await database.execute(query, data)
        return result
    except Exception as e:
        if type(e) is HTTPException:
            raise HTTPException(status_code=e.status_code,
                                detail=str(e.detail))
        raise HTTPException(status_code=500, detail=str(e))

async def get_address(data):
    try:
        query = open("./query/get_address.sql",
            "r",
        ).read()
        address = await database.execute(query, data)
        query = open("./query/get_user.sql",
            "r",
        ).read()
        result = await database.execute(query, data)
        # We get the response as a list with json value so we create a new feild for address and appends it to the json/dict
        result[0]['address'] = address 
        print(result[0],'\n\n',address)
        return result[0]
    except Exception as e:
        if type(e) is HTTPException:
            raise HTTPException(status_code=e.status_code,
                                detail=str(e.detail))
        raise HTTPException(status_code=500, detail=str(e))
        
async def user_in_specific_city(data):
    try:
        query = open("./query/user_in_specific_city.sql",
            "r",
        ).read()
        result = await database.execute(query, data)
        return result
    except Exception as e:
        if type(e) is HTTPException:
            raise HTTPException(status_code=e.status_code,
                                detail=str(e.detail))
        raise HTTPException(status_code=500, detail=str(e))

async def delete_address(data):
    try:
        query = open("./query/delete_address.sql",
            "r",
        ).read()
        result = await database.execute(query, data)
        return result
    except Exception as e:
        if type(e) is HTTPException:
            raise HTTPException(status_code=e.status_code,
                                detail=str(e.detail))
        raise HTTPException(status_code=500, detail=str(e))