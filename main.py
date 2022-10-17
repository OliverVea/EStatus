import logging

logging.basicConfig(filename='log.txt')

from elastic_status import StatusApp
from elastic_status.models import Configuration

Configuration.from_config('config.json')

StatusApp.run()
