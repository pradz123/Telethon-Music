import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "25080319"))
    API_HASH = os.environ.get("API_HASH", "ea2b0cb88be95a0416aa50c687a060e8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6079856797:AAFwTe7yURPCFk6g5yWEQ6H2V1rbmNx91a8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLgBu7gB0-rxGf6XgTRbFnoQhv2OLbta_fAZ2xua7hkjdbjx-AMnT8yc_DCiAFpiu2CDQX7GuxNrSfI7YpBRg_9uKzTx0l-g7e4Qc81KZXiJf6uf0SQefCurdv0ufHcm0d6BmfW_ZTFy2PlIoSS_6lXmxOoLaCMJzjQ_F6CBaLhjwgmGCr-VRqn4Vu5nWI_MKGjrFIFEbaoVV1CVf6zOOMGgKxOhs9VrfaTGxHQldHWHQN9ynkRCdAb5kfgyhyD-Nky1KzxDikleBpgGcFHMquKCCvtkR9zElsHxVLXefDx3CLAza7vQ-Pgyx4JWWQvhFX7UOshxLQuw4chwc3PSblLStsg=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RadiiiiasisBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6118334318")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
