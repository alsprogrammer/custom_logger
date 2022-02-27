import os
import sys
import logging

import structlog as sl

from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL_PARAMETER = 'LOG_LEVEL'
LOG_DESTINATION_PARAMETER = 'LOG_DESTINATION'

STD_OUTPUTS = {
    'stdout': sys.stdout,
    'stderr': sys.stderr,
}

LOG_LEVELS = {
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'WARNING': logging.WARN,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}

log_level = LOG_LEVELS.get(os.getenv(LOG_LEVEL_PARAMETER, logging.CRITICAL))
log_destination = os.getenv(LOG_DESTINATION_PARAMETER, 'stdout')

if log_destination in STD_OUTPUTS:
    logging.basicConfig(
        stream=STD_OUTPUTS[log_destination],
        format='%(message)s',
        level=log_level
    )
else:
    logging.basicConfig(
        filename=log_destination,
        format='%(message)s',
        level=log_level
    )

logger = sl.getLogger()

sl.configure(
    processors=[
        sl.stdlib.filter_by_level,
        sl.stdlib.add_logger_name,
        sl.stdlib.add_log_level,
        sl.stdlib.PositionalArgumentsFormatter(),
        sl.processors.TimeStamper(fmt="iso"),
        sl.processors.StackInfoRenderer(),
        sl.processors.format_exc_info,
        sl.processors.UnicodeDecoder(),
        sl.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=sl.stdlib.LoggerFactory(),
    wrapper_class=sl.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)
