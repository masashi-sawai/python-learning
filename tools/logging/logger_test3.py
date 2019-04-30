import logging

logging.basicConfig(level=logging.INFO)


# ログ専用クラスを作成し、logging.Filter の情報を継承させる
class NoPassFilter(logging.Filter):
    # フィルタ条件を設定する
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message

logger = logging.getLogger(__name__)
# logger プロパティにフィルタ情報を追加する
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main password = "test')
