import logging

# ログレベルを DEBUG に変更(これによりinfoとdebugもエラーとなる)
logging.basicConfig(level=logging.DEBUG)

logging.critical('クリティカル')
logging.error('通常エラー')
logging.warning('警告')
logging.info('インフォメーション')
logging.debug('デバッグ')
