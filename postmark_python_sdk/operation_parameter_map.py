operation_parameter_map = {
    '/bounces/{bounceid}/activate-PUT': {
        'parameters': [
            {
                'name': 'bounceid'
            },
        ]
    },
    '/bounces/{bounceid}-GET': {
        'parameters': [
            {
                'name': 'bounceid'
            },
        ]
    },
    '/deliverystats-GET': {
        'parameters': [
        ]
    },
    '/bounces/{bounceid}/dump-GET': {
        'parameters': [
            {
                'name': 'bounceid'
            },
        ]
    },
    '/bounces-GET': {
        'parameters': [
            {
                'name': 'count'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'type'
            },
            {
                'name': 'inactive'
            },
            {
                'name': 'emailFilter'
            },
            {
                'name': 'messageID'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'todate'
            },
            {
                'name': 'fromdate'
            },
        ]
    },
    '/triggers/inboundrules-POST': {
        'parameters': [
            {
                'name': 'Rule'
            },
        ]
    },
    '/triggers/inboundrules/{triggerid}-DELETE': {
        'parameters': [
            {
                'name': 'triggerid'
            },
        ]
    },
    '/triggers/inboundrules-GET': {
        'parameters': [
            {
                'name': 'count'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/messages/outbound/clicks-GET': {
        'parameters': [
            {
                'name': 'count'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'recipient'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'client_name'
            },
            {
                'name': 'client_company'
            },
            {
                'name': 'client_family'
            },
            {
                'name': 'os_name'
            },
            {
                'name': 'os_family'
            },
            {
                'name': 'os_company'
            },
            {
                'name': 'platform'
            },
            {
                'name': 'country'
            },
            {
                'name': 'region'
            },
            {
                'name': 'city'
            },
        ]
    },
    '/messages/inbound/{messageid}/details-GET': {
        'parameters': [
            {
                'name': 'messageid'
            },
        ]
    },
    '/messages/outbound/clicks/{messageid}-GET': {
        'parameters': [
            {
                'name': 'messageid'
            },
            {
                'name': 'count'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/messages/outbound/{messageid}/dump-GET': {
        'parameters': [
            {
                'name': 'messageid'
            },
        ]
    },
    '/messages/outbound/opens/{messageid}-GET': {
        'parameters': [
            {
                'name': 'messageid'
            },
            {
                'name': 'count'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/messages/outbound/{messageid}/details-GET': {
        'parameters': [
            {
                'name': 'messageid'
            },
        ]
    },
    '/messages/outbound/opens-GET': {
        'parameters': [
            {
                'name': 'count'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'recipient'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'client_name'
            },
            {
                'name': 'client_company'
            },
            {
                'name': 'client_family'
            },
            {
                'name': 'os_name'
            },
            {
                'name': 'os_family'
            },
            {
                'name': 'os_company'
            },
            {
                'name': 'platform'
            },
            {
                'name': 'country'
            },
            {
                'name': 'region'
            },
            {
                'name': 'city'
            },
        ]
    },
    '/messages/inbound/{messageid}/retry-PUT': {
        'parameters': [
            {
                'name': 'messageid'
            },
        ]
    },
    '/messages/inbound-GET': {
        'parameters': [
            {
                'name': 'count'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'recipient'
            },
            {
                'name': 'fromemail'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'mailboxhash'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'status'
            },
            {
                'name': 'todate'
            },
            {
                'name': 'fromdate'
            },
        ]
    },
    '/messages/outbound-GET': {
        'parameters': [
            {
                'name': 'count'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'recipient'
            },
            {
                'name': 'fromemail'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'status'
            },
            {
                'name': 'todate'
            },
            {
                'name': 'fromdate'
            },
        ]
    },
    '/messages/inbound/{messageid}/bypass-PUT': {
        'parameters': [
            {
                'name': 'messageid'
            },
        ]
    },
    '/email/batch-POST': {
        'parameters': [
        ]
    },
    '/email/batchWithTemplates-POST': {
        'parameters': [
            {
                'name': 'Messages'
            },
        ]
    },
    '/email/withTemplate-POST': {
        'parameters': [
            {
                'name': 'From'
            },
            {
                'name': 'TemplateAlias'
            },
            {
                'name': 'TemplateId'
            },
            {
                'name': 'TemplateModel'
            },
            {
                'name': 'To'
            },
            {
                'name': 'Attachments'
            },
            {
                'name': 'Bcc'
            },
            {
                'name': 'Cc'
            },
            {
                'name': 'Headers'
            },
            {
                'name': 'InlineCss'
            },
            {
                'name': 'ReplyTo'
            },
            {
                'name': 'Tag'
            },
            {
                'name': 'TrackLinks'
            },
            {
                'name': 'TrackOpens'
            },
        ]
    },
    '/email-POST': {
        'parameters': [
            {
                'name': 'Attachments'
            },
            {
                'name': 'Bcc'
            },
            {
                'name': 'Cc'
            },
            {
                'name': 'From'
            },
            {
                'name': 'Headers'
            },
            {
                'name': 'HtmlBody'
            },
            {
                'name': 'ReplyTo'
            },
            {
                'name': 'Subject'
            },
            {
                'name': 'Tag'
            },
            {
                'name': 'TextBody'
            },
            {
                'name': 'To'
            },
            {
                'name': 'TrackLinks'
            },
            {
                'name': 'TrackOpens'
            },
        ]
    },
    '/server-GET': {
        'parameters': [
        ]
    },
    '/server-PUT': {
        'parameters': [
            {
                'name': 'BounceHookUrl'
            },
            {
                'name': 'ClickHookUrl'
            },
            {
                'name': 'Color'
            },
            {
                'name': 'DeliveryHookUrl'
            },
            {
                'name': 'InboundDomain'
            },
            {
                'name': 'InboundHookUrl'
            },
            {
                'name': 'InboundSpamThreshold'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'OpenHookUrl'
            },
            {
                'name': 'PostFirstOpenOnly'
            },
            {
                'name': 'RawEmailEnabled'
            },
            {
                'name': 'SmtpApiActivated'
            },
            {
                'name': 'TrackLinks'
            },
            {
                'name': 'TrackOpens'
            },
        ]
    },
    '/stats/outbound/bounces-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/clicks/platforms-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/opens/emailclients-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/opens-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/opens/platforms-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/clicks-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/clicks/browserfamilies-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/clicks/location-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/sends-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/spam-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/stats/outbound/tracked-GET': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'fromdate'
            },
            {
                'name': 'todate'
            },
        ]
    },
    '/templates-POST': {
        'parameters': [
            {
                'name': 'Name'
            },
            {
                'name': 'Subject'
            },
            {
                'name': 'Alias'
            },
            {
                'name': 'HtmlBody'
            },
            {
                'name': 'TextBody'
            },
        ]
    },
    '/templates/{templateIdOrAlias}-DELETE': {
        'parameters': [
            {
                'name': 'templateIdOrAlias'
            },
        ]
    },
    '/templates/{templateIdOrAlias}-GET': {
        'parameters': [
            {
                'name': 'templateIdOrAlias'
            },
        ]
    },
    '/templates-GET': {
        'parameters': [
            {
                'name': 'Count'
            },
            {
                'name': 'Offset'
            },
        ]
    },
    '/email/batchWithTemplates-POST': {
        'parameters': [
            {
                'name': 'Messages'
            },
        ]
    },
    '/email/withTemplate-POST': {
        'parameters': [
            {
                'name': 'From'
            },
            {
                'name': 'TemplateAlias'
            },
            {
                'name': 'TemplateId'
            },
            {
                'name': 'TemplateModel'
            },
            {
                'name': 'To'
            },
            {
                'name': 'Attachments'
            },
            {
                'name': 'Bcc'
            },
            {
                'name': 'Cc'
            },
            {
                'name': 'Headers'
            },
            {
                'name': 'InlineCss'
            },
            {
                'name': 'ReplyTo'
            },
            {
                'name': 'Tag'
            },
            {
                'name': 'TrackLinks'
            },
            {
                'name': 'TrackOpens'
            },
        ]
    },
    '/templates/{templateIdOrAlias}-PUT': {
        'parameters': [
            {
                'name': 'templateIdOrAlias'
            },
            {
                'name': 'Alias'
            },
            {
                'name': 'HtmlBody'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'Subject'
            },
            {
                'name': 'TextBody'
            },
        ]
    },
    '/templates/validate-POST': {
        'parameters': [
            {
                'name': 'HtmlBody'
            },
            {
                'name': 'InlineCssForHtmlTestRender'
            },
            {
                'name': 'Subject'
            },
            {
                'name': 'TestRenderModel'
            },
            {
                'name': 'TextBody'
            },
        ]
    },
};