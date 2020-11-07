import argparse
from modules import common
import logging

FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger()
parser = argparse.ArgumentParser(description='Приклад передачі аргументів у Python програму.')
parser.add_argument('-o', '--optional', dest='opt', type=str, help='Цей параметр є вибірковим.')
parser.add_argument('-l', '--logs', dest='logs', action='store_true',
                    help='Якщо виконати команду з цим параметром будуть виводитись логи.')


def main(text):
    print(f"We are in the {__name__}")
    print(common.get_current_date().now())
    print(common.get_current_platform())
    if text:
        print("З консолі було передано аргумент\n", 10*"=", f">> {text} <<", 10*"=")


def how_to_write_logs():
    logger.info("Тут буде просто інформативне повідомлення")
    logger.warning("Це Warning повідомлення")
    logger.error("Це повідомлення про помилку")

def def1(a):
    try:
       print("Що буде якщо a*(-1))", -a, "?")
    except Exception as e:
        logger.error("Це повідомлення про помилку")
        print(e)
    else:
        logger.info("Тут буде просто інформативне повідомлення")
    finally:
        print("А вот воно що!")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.logs:
        how_to_write_logs()
    else:
        main(args.opt)
    common.from_1_to_100(False)
    common.from_1_to_100(True)
    def1(4)
    def1([3,4,5])


