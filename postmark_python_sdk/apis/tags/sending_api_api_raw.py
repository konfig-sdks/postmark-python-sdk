# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from postmark_python_sdk.paths.email_batch.post import SendBatchEmailsRaw
from postmark_python_sdk.paths.email_batch_with_templates.post import SendBatchWithTemplatesRaw
from postmark_python_sdk.paths.email_with_template.post import SendEmailTemplateRaw
from postmark_python_sdk.paths.email.post import SendSingleEmailRaw


class SendingAPIApiRaw(
    SendBatchEmailsRaw,
    SendBatchWithTemplatesRaw,
    SendEmailTemplateRaw,
    SendSingleEmailRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
