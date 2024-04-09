import logging

logging.basicConfig(
    filename = 'log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

for i in range(10):
    # print(i)
    logging.info(f'{i=}')
    logging.debug(f'{i=}') # print
    logging.warning(f'{i=}')
    logging.error(f'{i=}')
    logging.critical(f'{i=}')