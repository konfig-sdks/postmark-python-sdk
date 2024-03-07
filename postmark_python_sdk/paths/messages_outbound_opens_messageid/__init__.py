# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from postmark_python_sdk.paths.messages_outbound_opens_messageid import Api

from postmark_python_sdk.paths import PathValues

path = PathValues.MESSAGES_OUTBOUND_OPENS_MESSAGEID