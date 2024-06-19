from fastapi import APIRouter,Depends,Response,status
from ..Dependencies.Dependencies import verify_token
from ..db.db import Connect_mongo
from ..Models.Notes import Notes
from bson import ObjectId
router = APIRouter(prefix="/note")
import json
@router.post("/createnote")
def crete(respond:Response,note:Notes , check: dict = Depends(verify_token)):
    try:
        if(not check): return
        note.user = check["id"]
        data  = Connect_mongo()["notes"]
        data.insert_one(dict(note))
        respond.status_code = status.HTTP_201_CREATED
        return (dict(note))
    except Exception as e:
        print(e)
        respond.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return "Something wrong"
@router.get("/fetchnote")
def fetch(respond:Response, check: dict = Depends(verify_token)):
    if(not check): return
    data  = Connect_mongo()["notes"]
    notes = list(data.find({"user":check['id']},{"_id":0}))
    return notes

@router.put("/updatenote/{id}")
def fetch(respond:Response,update:dict,id:str ,check: dict = Depends(verify_token)):
    if(not check): return
    data = Connect_mongo()["notes"]
    NoteId = data.find_one({"_id":ObjectId(id)})
    if (NoteId == None):
        respond.status_code = status.HTTP_404_NOT_FOUND
        return "not found"
    if NoteId["user"] != (check["id"]):
        respond.status_code = status.HTTP_401_UNAUTHORIZED
        return ("Don't allowed This")
    data.find_one_and_update(data.find_one({"_id":ObjectId(id)}),{'$set':update})

@router.delete("/deletenote/{id}")
def fetch(respond:Response,id:str ,check: dict = Depends(verify_token)):
    if(not check): return
    data = Connect_mongo()["notes"]
    NoteId = data.find_one({"_id":ObjectId(id)})
    if (NoteId == None):
        respond.status_code = status.HTTP_404_NOT_FOUND
        return "not found"
    if NoteId["user"] != (check["id"]):
        respond.status_code = status.HTTP_401_UNAUTHORIZED
        return ("Don't allowed This")
    data.find_one_and_delete(data.find_one({"_id":ObjectId(id)}))
    respond.status_code = status.HTTP_200_OK
    return ("delete sucessfully")