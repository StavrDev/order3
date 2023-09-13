from utils import TgBot
from kb import kb_start, kb_set_time

api_id = 22239809
api_hash = 'fc57726d589788687fc518260cfe176d'
TokenBot = '6392188988:AAGEksJrweYY1AhoL1bgNdcAcqGBmrIaDKc'

app = TgBot(TokenBot, kb_start, kb_set_time, api_id, api_hash)

if __name__ == "__main__":
    app.start()