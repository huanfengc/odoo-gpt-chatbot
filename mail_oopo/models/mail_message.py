from odoo import fields, models, api

class Message(models.Model):
    _inherit = "mail.message"

    message_type = fields.Selection(selection_add=[("bot_function", "Function Call"), ("bot_function_request", "Function Request")], ondelete={"bot_function": "set default", "bot_function_request": "set default"})
    function_content = fields.Json(string="Function Content", help="Function Content")

    def _get_message_format_fields(self):
        res = super(Message, self)._get_message_format_fields()
        res.append("function_content")
        return res