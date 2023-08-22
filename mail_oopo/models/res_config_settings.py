from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    openai_api_key = fields.Char(string="OpenAI API Key", config_parameter="mail_oopo.openapi_api_key")