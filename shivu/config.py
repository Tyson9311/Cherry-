class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7859078565"
    sudo_users = "5469324918", "5617176795"
    GROUP_ID = -1002593258889
    TOKEN = "7847731366:AAEq8Wbe2nx3oqqyIxwRI_-ABwEVSWdvfq0"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Shadow_official_group"
    UPDATE_CHAT = "Shadow_support_official"
    BOT_USERNAME = "Shadow_hunterbot"
    CHARA_CHANNEL_ID = "2608151037"
    api_id = 25144375
    api_hash = "70ff034329e28259cd85a988a6fa395e"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
