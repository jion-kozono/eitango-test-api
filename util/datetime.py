from datetime import datetime


def get_now():
    now = datetime.now()
    now_format = str(now.strftime('%Y年%m月%d日%H時%M分'))
    return now_format # yyyyMMddHHmmss形式で出力