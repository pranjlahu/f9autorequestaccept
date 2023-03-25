from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "19631923"))
    API_HASH = getenv("API_HASH", "027b7feb0a8f9822e53af59706b8f635")
    BOT_TOKEN = getenv("BOT_TOKEN", "5989401655:AAFXjsC51YGClf_xv-fHMc4fZlu2i7JJaus")
    FSUB = getenv("FSUB", "F9Devs")
    CHID = int(getenv("CHID", "-1001536495904"))
    SUDO = list(map(int, getenv("SUDO", "6029941553","1217302537").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb://samar:samar@ac-sjxwrus-shard-00-00.ayer8ux.mongodb.net:27017,ac-sjxwrus-shard-00-01.ayer8ux.mongodb.net:27017,ac-sjxwrus-shard-00-02.ayer8ux.mongodb.net:27017/?ssl=true&replicaSet=atlas-ghv0w6-shard-0&authSource=admin&retryWrites=true&w=majority")
    
cfg = Config()
