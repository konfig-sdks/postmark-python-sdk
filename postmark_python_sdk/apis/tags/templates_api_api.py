# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from postmark_python_sdk.paths.templates.post import CreateTemplate
from postmark_python_sdk.paths.templates_template_id_or_alias.delete import DeleteTemplate
from postmark_python_sdk.paths.templates_template_id_or_alias.get import GetTemplateById
from postmark_python_sdk.paths.templates.get import ListTemplates
from postmark_python_sdk.paths.email_batch_with_templates.post import SendBatchWithTemplates
from postmark_python_sdk.paths.email_with_template.post import SendEmailTemplate
from postmark_python_sdk.paths.templates_template_id_or_alias.put import UpdateTemplate
from postmark_python_sdk.paths.templates_validate.post import ValidateTemplateContent
from postmark_python_sdk.apis.tags.templates_api_api_raw import TemplatesAPIApiRaw


class TemplatesAPIApi(
    CreateTemplate,
    DeleteTemplate,
    GetTemplateById,
    ListTemplates,
    SendBatchWithTemplates,
    SendEmailTemplate,
    UpdateTemplate,
    ValidateTemplateContent,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TemplatesAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TemplatesAPIApiRaw(api_client)
