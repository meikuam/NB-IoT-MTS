import os
import json
from pandas.tseries.offsets import DateOffset
from dateutil.relativedelta import relativedelta
from pathlib import Path
from threading import Thread


def project_root() -> Path:
    """return project dir path"""
    return Path(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        )
    )


with open(os.path.join(project_root(), "config.json")) as json_file:
    config = json.load(json_file)
