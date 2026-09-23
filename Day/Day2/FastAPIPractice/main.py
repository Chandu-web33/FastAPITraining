from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message":"Hello World":"number":44,"is_fun":True}
@app.get("/about")
def about():
    return {"page":"About","author":"Chandan"}
@app.get("/health")
def health():
    return {"status":"ok"}
@app.get("/student/{usn}")
def get_result(usn):
    return {"message":"Created"}

@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","usn":usn}
@app.get("/candidate/{usn}")
def get_candidate(rollno:int):
    return {"Result":"Distinction","rollno":rollno,,"type":str(type(rollno))}

class Item(BaseModel):
    name:str
    price:float
    in_stock: bool = True
    
@app.post("/items")
def create_item(item:Item): 
    return {"received":item,"total_price":item.price*1.18} 
