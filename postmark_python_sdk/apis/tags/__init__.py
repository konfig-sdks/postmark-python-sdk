# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from postmark_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    STATS_API = "Stats API"
    MESSAGES_API = "Messages API"
    TEMPLATES_API = "Templates API"
    BOUNCES_API = "Bounces API"
    SENDING_API = "Sending API"
    INBOUND_RULES_API = "Inbound Rules API"
    SERVER_CONFIGURATION_API = "Server Configuration API"
