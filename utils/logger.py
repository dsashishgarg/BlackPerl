import os
import sys
import logging
import logging.handlers
from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


def get_logger(name):
    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)-15s -' + name + ' - %(filename)s - %(levelname)s : %(funcName)s() %(message)s')
        handler1 = logging.StreamHandler(stream=sys.stdout)
        handler = logging.handlers.WatchedFileHandler(
            os.environ.get("LOGFILE", "BlackPerl.log"))
        handler.setFormatter(formatter)
        handler1.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(handler1)
    return logger


class ApiStatus(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class ApiName(str, Enum):
    getall = "Get all Prodcuts"
    post = "Create a Single Product"
    get = "Get Single Prodcuts"
    delete = "Delete Single Product"


class LogDetails(BaseModel):
    api_name: Optional[ApiName] = "NA"
    api_status: Optional[ApiStatus] = "NA"
    status_code: Optional[str] = "NA"
    elapse_time: Optional[str] = "NA"
    start_time: Optional[datetime]
    message: Optional[str] = "NA"


LOG = get_logger(__name__)


def log_details_to_string(log_details: LogDetails):

    log_details_to_string = "{}|{}|{}|{}|{}".format(
        log_details.api_name, log_details.api_status, log_details.status_code, log_details.elapse_time, log_details.message)
    return log_details_to_string


def api_response_time(log_details: LogDetails):
    end = datetime.now()
    time_taken = end - log_details.start_time
    time_ms = time_taken.total_seconds()*1000
    log_details.elapse_time = "{:.2f}".format(time_ms)
    LOG.info("{}|{}|{}|{}|{}".format(
        log_details.api_name, log_details.api_status, log_details.status_code, log_details.elapse_time, log_details.message))
