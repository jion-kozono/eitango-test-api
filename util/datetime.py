from datetime import datetime, timezone, timedelta

def get_now():
    now = datetime.now(timezone(timedelta(hours=+9), 'JST'))
    now_format = str(now.strftime('%Y年%m月%d日%H時%M分'))
    return now_format # yyyyMMddHHmmss形式で出力