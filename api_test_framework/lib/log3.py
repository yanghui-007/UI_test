import logging

logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log/log.txt',  # 日志输出文件
                    filemode='a')  # 追加模式



logging.debug('debug info')
logging.info('hello 宏哥')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')

  
if __name__ == '__main__':
    logging.info("hello")




