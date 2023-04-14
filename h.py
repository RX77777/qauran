from pyrogram import Client

api_id = "22173725" 
api_hash = "375509c9487bdda2bcaf803f0223d5bc"
bot_token = "5962156884:AAEBOd5crk8SWWQFZueWVOs2m_-Bx_UXBRM"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
