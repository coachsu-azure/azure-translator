import os
import pathlib
from dotenv import load_dotenv
from flask import Flask, request, render_template
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

# 如果.env存在，讀取.env檔案
env_path = pathlib.Path(".env")
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# 取得環境變數
REGION = os.getenv('REGION')
KEY = os.getenv('KEY')
ENDPOINT = os.getenv('ENDPOINT')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def translator():

    SRC = request.args.get('src')
    TEXT = request.args.get('text')
    DST = request.args.get('dst')

    if SRC and TEXT and DST:
        client = TextTranslationClient(
            endpoint=ENDPOINT,
            credential=TranslatorCredential(KEY, REGION)
        )

        src = SRC # 來源語言
        dst = [DST] # 目標語言(可多個)
        targets = [InputTextItem(text=TEXT)] # 目標文字(可多個)
        responses = client.translate(content=targets, to=dst, from_parameter=src)
        translation = responses[0].translations[0]
        translated_text=translation.text

        return translated_text

    return "Please provide src, text, and dst parameters."

if __name__ == '__main__':
    print(REGION, KEY, ENDPOINT)
    app.run(host='0.0.0.0', port=8080)
