import typing_extensions

from postmark_python_sdk.apis.tags import TagValues
from postmark_python_sdk.apis.tags.stats_api_api import StatsAPIApi
from postmark_python_sdk.apis.tags.messages_api_api import MessagesAPIApi
from postmark_python_sdk.apis.tags.templates_api_api import TemplatesAPIApi
from postmark_python_sdk.apis.tags.bounces_api_api import BouncesAPIApi
from postmark_python_sdk.apis.tags.sending_api_api import SendingAPIApi
from postmark_python_sdk.apis.tags.inbound_rules_api_api import InboundRulesAPIApi
from postmark_python_sdk.apis.tags.server_configuration_api_api import ServerConfigurationAPIApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.STATS_API: StatsAPIApi,
        TagValues.MESSAGES_API: MessagesAPIApi,
        TagValues.TEMPLATES_API: TemplatesAPIApi,
        TagValues.BOUNCES_API: BouncesAPIApi,
        TagValues.SENDING_API: SendingAPIApi,
        TagValues.INBOUND_RULES_API: InboundRulesAPIApi,
        TagValues.SERVER_CONFIGURATION_API: ServerConfigurationAPIApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.STATS_API: StatsAPIApi,
        TagValues.MESSAGES_API: MessagesAPIApi,
        TagValues.TEMPLATES_API: TemplatesAPIApi,
        TagValues.BOUNCES_API: BouncesAPIApi,
        TagValues.SENDING_API: SendingAPIApi,
        TagValues.INBOUND_RULES_API: InboundRulesAPIApi,
        TagValues.SERVER_CONFIGURATION_API: ServerConfigurationAPIApi,
    }
)
