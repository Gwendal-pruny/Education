import os
import json

DATA = json.load(
    open(
        os.path.dirname(
            os.path.realpath(__file__)
        ) + "/data.json"
    )
)

def _make_messages():
    messages = {}

    for entity_name, entity_prefix in DATA["prefixes"].items():
        entity_messages = {}

        for message_name, message in DATA["templates"].items():
            entity_messages[message_name] = entity_prefix + " " + message

        messages[entity_name] = entity_messages

    return messages

DATA["messages"] = _make_messages()