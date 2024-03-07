import typing_extensions

from postmark_python_sdk.paths import PathValues
from postmark_python_sdk.apis.paths.bounces import Bounces
from postmark_python_sdk.apis.paths.bounces_bounceid import BouncesBounceid
from postmark_python_sdk.apis.paths.bounces_bounceid_activate import BouncesBounceidActivate
from postmark_python_sdk.apis.paths.bounces_bounceid_dump import BouncesBounceidDump
from postmark_python_sdk.apis.paths.deliverystats import Deliverystats
from postmark_python_sdk.apis.paths.email import Email
from postmark_python_sdk.apis.paths.email_batch import EmailBatch
from postmark_python_sdk.apis.paths.email_batch_with_templates import EmailBatchWithTemplates
from postmark_python_sdk.apis.paths.email_with_template import EmailWithTemplate
from postmark_python_sdk.apis.paths.messages_inbound import MessagesInbound
from postmark_python_sdk.apis.paths.messages_inbound_messageid_bypass import MessagesInboundMessageidBypass
from postmark_python_sdk.apis.paths.messages_inbound_messageid_details import MessagesInboundMessageidDetails
from postmark_python_sdk.apis.paths.messages_inbound_messageid_retry import MessagesInboundMessageidRetry
from postmark_python_sdk.apis.paths.messages_outbound import MessagesOutbound
from postmark_python_sdk.apis.paths.messages_outbound_clicks import MessagesOutboundClicks
from postmark_python_sdk.apis.paths.messages_outbound_clicks_messageid import MessagesOutboundClicksMessageid
from postmark_python_sdk.apis.paths.messages_outbound_opens import MessagesOutboundOpens
from postmark_python_sdk.apis.paths.messages_outbound_opens_messageid import MessagesOutboundOpensMessageid
from postmark_python_sdk.apis.paths.messages_outbound_messageid_details import MessagesOutboundMessageidDetails
from postmark_python_sdk.apis.paths.messages_outbound_messageid_dump import MessagesOutboundMessageidDump
from postmark_python_sdk.apis.paths.server import Server
from postmark_python_sdk.apis.paths.stats_outbound import StatsOutbound
from postmark_python_sdk.apis.paths.stats_outbound_bounces import StatsOutboundBounces
from postmark_python_sdk.apis.paths.stats_outbound_clicks import StatsOutboundClicks
from postmark_python_sdk.apis.paths.stats_outbound_clicks_browserfamilies import StatsOutboundClicksBrowserfamilies
from postmark_python_sdk.apis.paths.stats_outbound_clicks_location import StatsOutboundClicksLocation
from postmark_python_sdk.apis.paths.stats_outbound_clicks_platforms import StatsOutboundClicksPlatforms
from postmark_python_sdk.apis.paths.stats_outbound_opens import StatsOutboundOpens
from postmark_python_sdk.apis.paths.stats_outbound_opens_emailclients import StatsOutboundOpensEmailclients
from postmark_python_sdk.apis.paths.stats_outbound_opens_platforms import StatsOutboundOpensPlatforms
from postmark_python_sdk.apis.paths.stats_outbound_sends import StatsOutboundSends
from postmark_python_sdk.apis.paths.stats_outbound_spam import StatsOutboundSpam
from postmark_python_sdk.apis.paths.stats_outbound_tracked import StatsOutboundTracked
from postmark_python_sdk.apis.paths.templates import Templates
from postmark_python_sdk.apis.paths.templates_validate import TemplatesValidate
from postmark_python_sdk.apis.paths.templates_template_id_or_alias import TemplatesTemplateIdOrAlias
from postmark_python_sdk.apis.paths.triggers_inboundrules import TriggersInboundrules
from postmark_python_sdk.apis.paths.triggers_inboundrules_triggerid import TriggersInboundrulesTriggerid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.BOUNCES: Bounces,
        PathValues.BOUNCES_BOUNCEID: BouncesBounceid,
        PathValues.BOUNCES_BOUNCEID_ACTIVATE: BouncesBounceidActivate,
        PathValues.BOUNCES_BOUNCEID_DUMP: BouncesBounceidDump,
        PathValues.DELIVERYSTATS: Deliverystats,
        PathValues.EMAIL: Email,
        PathValues.EMAIL_BATCH: EmailBatch,
        PathValues.EMAIL_BATCH_WITH_TEMPLATES: EmailBatchWithTemplates,
        PathValues.EMAIL_WITH_TEMPLATE: EmailWithTemplate,
        PathValues.MESSAGES_INBOUND: MessagesInbound,
        PathValues.MESSAGES_INBOUND_MESSAGEID_BYPASS: MessagesInboundMessageidBypass,
        PathValues.MESSAGES_INBOUND_MESSAGEID_DETAILS: MessagesInboundMessageidDetails,
        PathValues.MESSAGES_INBOUND_MESSAGEID_RETRY: MessagesInboundMessageidRetry,
        PathValues.MESSAGES_OUTBOUND: MessagesOutbound,
        PathValues.MESSAGES_OUTBOUND_CLICKS: MessagesOutboundClicks,
        PathValues.MESSAGES_OUTBOUND_CLICKS_MESSAGEID: MessagesOutboundClicksMessageid,
        PathValues.MESSAGES_OUTBOUND_OPENS: MessagesOutboundOpens,
        PathValues.MESSAGES_OUTBOUND_OPENS_MESSAGEID: MessagesOutboundOpensMessageid,
        PathValues.MESSAGES_OUTBOUND_MESSAGEID_DETAILS: MessagesOutboundMessageidDetails,
        PathValues.MESSAGES_OUTBOUND_MESSAGEID_DUMP: MessagesOutboundMessageidDump,
        PathValues.SERVER: Server,
        PathValues.STATS_OUTBOUND: StatsOutbound,
        PathValues.STATS_OUTBOUND_BOUNCES: StatsOutboundBounces,
        PathValues.STATS_OUTBOUND_CLICKS: StatsOutboundClicks,
        PathValues.STATS_OUTBOUND_CLICKS_BROWSERFAMILIES: StatsOutboundClicksBrowserfamilies,
        PathValues.STATS_OUTBOUND_CLICKS_LOCATION: StatsOutboundClicksLocation,
        PathValues.STATS_OUTBOUND_CLICKS_PLATFORMS: StatsOutboundClicksPlatforms,
        PathValues.STATS_OUTBOUND_OPENS: StatsOutboundOpens,
        PathValues.STATS_OUTBOUND_OPENS_EMAILCLIENTS: StatsOutboundOpensEmailclients,
        PathValues.STATS_OUTBOUND_OPENS_PLATFORMS: StatsOutboundOpensPlatforms,
        PathValues.STATS_OUTBOUND_SENDS: StatsOutboundSends,
        PathValues.STATS_OUTBOUND_SPAM: StatsOutboundSpam,
        PathValues.STATS_OUTBOUND_TRACKED: StatsOutboundTracked,
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_VALIDATE: TemplatesValidate,
        PathValues.TEMPLATES_TEMPLATE_ID_OR_ALIAS: TemplatesTemplateIdOrAlias,
        PathValues.TRIGGERS_INBOUNDRULES: TriggersInboundrules,
        PathValues.TRIGGERS_INBOUNDRULES_TRIGGERID: TriggersInboundrulesTriggerid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.BOUNCES: Bounces,
        PathValues.BOUNCES_BOUNCEID: BouncesBounceid,
        PathValues.BOUNCES_BOUNCEID_ACTIVATE: BouncesBounceidActivate,
        PathValues.BOUNCES_BOUNCEID_DUMP: BouncesBounceidDump,
        PathValues.DELIVERYSTATS: Deliverystats,
        PathValues.EMAIL: Email,
        PathValues.EMAIL_BATCH: EmailBatch,
        PathValues.EMAIL_BATCH_WITH_TEMPLATES: EmailBatchWithTemplates,
        PathValues.EMAIL_WITH_TEMPLATE: EmailWithTemplate,
        PathValues.MESSAGES_INBOUND: MessagesInbound,
        PathValues.MESSAGES_INBOUND_MESSAGEID_BYPASS: MessagesInboundMessageidBypass,
        PathValues.MESSAGES_INBOUND_MESSAGEID_DETAILS: MessagesInboundMessageidDetails,
        PathValues.MESSAGES_INBOUND_MESSAGEID_RETRY: MessagesInboundMessageidRetry,
        PathValues.MESSAGES_OUTBOUND: MessagesOutbound,
        PathValues.MESSAGES_OUTBOUND_CLICKS: MessagesOutboundClicks,
        PathValues.MESSAGES_OUTBOUND_CLICKS_MESSAGEID: MessagesOutboundClicksMessageid,
        PathValues.MESSAGES_OUTBOUND_OPENS: MessagesOutboundOpens,
        PathValues.MESSAGES_OUTBOUND_OPENS_MESSAGEID: MessagesOutboundOpensMessageid,
        PathValues.MESSAGES_OUTBOUND_MESSAGEID_DETAILS: MessagesOutboundMessageidDetails,
        PathValues.MESSAGES_OUTBOUND_MESSAGEID_DUMP: MessagesOutboundMessageidDump,
        PathValues.SERVER: Server,
        PathValues.STATS_OUTBOUND: StatsOutbound,
        PathValues.STATS_OUTBOUND_BOUNCES: StatsOutboundBounces,
        PathValues.STATS_OUTBOUND_CLICKS: StatsOutboundClicks,
        PathValues.STATS_OUTBOUND_CLICKS_BROWSERFAMILIES: StatsOutboundClicksBrowserfamilies,
        PathValues.STATS_OUTBOUND_CLICKS_LOCATION: StatsOutboundClicksLocation,
        PathValues.STATS_OUTBOUND_CLICKS_PLATFORMS: StatsOutboundClicksPlatforms,
        PathValues.STATS_OUTBOUND_OPENS: StatsOutboundOpens,
        PathValues.STATS_OUTBOUND_OPENS_EMAILCLIENTS: StatsOutboundOpensEmailclients,
        PathValues.STATS_OUTBOUND_OPENS_PLATFORMS: StatsOutboundOpensPlatforms,
        PathValues.STATS_OUTBOUND_SENDS: StatsOutboundSends,
        PathValues.STATS_OUTBOUND_SPAM: StatsOutboundSpam,
        PathValues.STATS_OUTBOUND_TRACKED: StatsOutboundTracked,
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_VALIDATE: TemplatesValidate,
        PathValues.TEMPLATES_TEMPLATE_ID_OR_ALIAS: TemplatesTemplateIdOrAlias,
        PathValues.TRIGGERS_INBOUNDRULES: TriggersInboundrules,
        PathValues.TRIGGERS_INBOUNDRULES_TRIGGERID: TriggersInboundrulesTriggerid,
    }
)
