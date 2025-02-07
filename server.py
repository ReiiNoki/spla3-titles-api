import os

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pymongo import MongoClient

app = FastAPI()

# CORS 中间件解决跨域请求问题
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
ATLAS_URI = os.getenv('ATLAS_URI')
DB_NAME = 'spla3_titles'
ADJ = 'adjectives'
SUB = 'subject'

DESCRIPTION = '''Language code in ISO 639-1 format.
                 Language supported: zh-CN, de, en, es, fr, it, nl, ru, ja, ko, zh-TW, en-US, es-Us, fr-CA.
                 If not specified, the title will be generated in ALL supported languages.'''

client = MongoClient(ATLAS_URI)
db = client[DB_NAME]
collection_adj = db[ADJ]
collection_sub = db[SUB]

idx = 101
adjs = None
subs = None

LANG_MAP = {
    "zh-CN": "CNzh",  # 中文（简体）
    "de": "EUde",     # 德语
    "en": "EUen",     # 英语（欧洲）
    "es": "EUes",     # 西班牙语（欧洲）
    "fr": "EUfr",     # 法语（欧洲）
    "it": "EUit",     # 意大利语
    "nl": "EUnl",     # 荷兰语
    "ru": "EUru",     # 俄语
    "ja": "JPja",     # 日语
    "ko": "KRko",     # 韩语
    "zh-TW": "TWzh",  # 中文（繁体）
    "en-US": "USen",  # 英语（美国）
    "es-US": "USes",  # 西班牙语（美国）
    "fr-CA": "USfr"   # 法语（加拿大）
}

@app.get("/title/")
@app.get("/title/{lang}")
def get_random_title(lang: str = None) -> dict:
    
    global idx, adjs, subs
    if idx > 100:
        adjs = list(collection_adj.aggregate([{ "$sample": { "size": 100 } }]))
        subs = list(collection_sub.aggregate([{ "$sample": { "size": 100 } }]))
        idx = 0
    else:
        idx += 1
    
    if lang in LANG_MAP.keys():
        lang = LANG_MAP[lang]
        return {"title": {"adjective": f"{adjs[idx][lang]}", "subject": f"{subs[idx][lang]}"}}
    return {"title": {"adjective": f"{adjs[idx]}", "subject": f"{subs[idx]}"}}