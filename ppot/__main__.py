'''
 P-Pot
    Description:
         This is a test for Honey pots in primary stages used for teaching methods
    Author: Faysal Al-Banna
    E-Mail: degreane@gmail.com
    Usage:
    python3 -m ppot

    configuration ini file :
        /etc/ppot/ppot.ini
        [default]
            - ports = 8088, 8089
'''
import configparser
from ppot import HoneyPot
import logging

def setup_logger(logfile):
    logger=logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    loggerHandler=logging.FileHandler(logfile,mode="a")
    formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s')
    loggerHandler.setFormatter(formatter)
    logger.addHandler(loggerHandler)
    return logger


config_file="cfg.ini"
config=configparser.ConfigParser()
config.read(config_file)
ports=config.get('default','ports',raw=True,fallback="6910,6911").split(',')
logfile=config.get('default','logfile',raw=True,fallback="ppot.log")
bindIP=config.get('default','ip',raw=True,fallback="0.0.0.0")
logger=setup_logger(logfile)
logger.debug("Configured Ports {0}".format(ports))


pot=HoneyPot(ports,bindIP,logger)
pot.run()