"""
interface json
"""

import os
import json

DATA = json.load(
    open(
        os.path.dirname(
            os.path.realpath(__file__)
        ) + "/data.json"
    )
)
