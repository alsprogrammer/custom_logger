=====
Usage
=====

To use custom_logger in a project::

    from custom_logger import logging

    logger = logging.getLogger(__name__)

    logging.debug("This is a debug message", extra_parameter="extra parameter")
