from flask import Flask, request
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

# 以下資訊可以從 Azure 翻譯服務取得(正式上線時不要直接把金鑰跟服務端點寫在程式碼裡)
REGION = '[填入區域]' # 區域
KEY = '[填入金鑰]' # 金鑰
ENDPOINT = '[填入服務端點]' # 服務端點

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def translator():
    SRC = request.args.get('src')
    DST = request.args.get('dst')
    TARGET = request.args.get('target')

    client = TextTranslationClient(
        endpoint=ENDPOINT,
        credential=TranslatorCredential(KEY, REGION)
    )

    src = SRC # 來源語言
    dst = [DST] # 目標語言(可多個)
    targets = [InputTextItem(text=TARGET)] # 目標文字(可多個)
    responses = client.translate(content=targets, to=dst, from_parameter=src)
    translation = responses[0].translations[0]
    return "[{}] {}".format(translation.to, translation.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
