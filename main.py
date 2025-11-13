from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/test/")
def test_1():
     return {"msg":"hi from test"}

@app.get("/test/")
def test_2(name:str):
     return {"msg": "saved user"}

@app.get("/test/")
def test_3(name:str):
     user=name
     with open("names", "a") as f:
         f.write(user)
     return user

@app.get("/test/")
def Caesar(text:str,offset:int,mode:str):
    list_1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in text:
        if i in list_1:
            if mode == 'encryption':
                if list_1.index(i)+offset+1<=len(list_1):
                    text[i]=list_1[list_1.index(i)+offset]
                else:
                    text[i]=list_1[list_1.index(i)+offset+1-len(list_1)]
            elif mode=='decryption':
                if offset<list_1.index(i)+1:
                    text[i]=list_1[list_1.index(i)-offset]
                else:
                    text[i]=list_1[len(list_1)-1-(offset-list_1.index(i))]
    return text







