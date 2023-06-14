"""
スレッドの確認
スレッドを理解した後は、セマフォを参照
"""
import logging
import time
from threading import Thread

logging.basicConfig(level=logging.INFO)

def do_this():
	logging.info('Starting this!')
	time.sleep(2)
	logging.info('Did this.')
	
def do_that():
	logging.info('Starting that!')
	time.sleep(3)
	logging.info('Did that.')

# スレッド適用しない場合
# do_this()
# do_that()

# スレッドの動きチェック
t1 = Thread(target=do_this)
t1.start()
t2 = Thread(target=do_that)
t2.start()
