import logging

def get_logger(pgm_name):

    logfmt = '[%(asctime)s][%(levelname)s][%(name)s] %(message)s'
    logging.basicConfig( filename = pgm_name+'.debug.log',filemode = 'a'
                        ,level = logging.DEBUG,
                        format = logfmt,
                        datefmt = '%Y-%m-%d %H:%M:%S' )
    # 로그 생성
    logger = logging.getLogger(pgm_name)
    logger.setLevel(logging.INFO)

    # log 출력 형식
    formatter = logging.Formatter(logfmt)

    # 콘솔 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    # 파일 출력
    file_handler = logging.FileHandler(pgm_name+'.info.log',encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger