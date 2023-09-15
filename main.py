from utils import TgBot
from kb import kb_start, kb_set_time, kb_m, kb_days, kb_time

api_id = 'api_id'
api_hash = api_hash
TokenBot = TokenBot

app = TgBot(TokenBot, kb_start, kb_set_time, api_id, api_hash, kb_m, kb_time, kb_days)

if __name__ == "__main__":
    app.start()