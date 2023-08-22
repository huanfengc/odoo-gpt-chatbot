from odoo import models, fields, _

class Users(models.Model):
    _inherit = "res.users"

    system_prompt = "Oopo: Hello- I am Oopo a friendly AI Assistant, feel free to ask me any questions, or ask to perform any action."

    oopo_state = fields.Selection(
        [
            ("not_initialized", "Not initialized"),
            ("idle", "Idle"),
            ("disabled", "Disabled"),
        ], string="Oopo AI Status", required=False, default="not_initialized")
    
    openai_model = fields.Selection([("gpt-3.5-turbo-0613", "4k Context Model"),("gpt-3.5-turbo-16k", "16k Context Model"), ("gpt-4", "GPT4 8k")], string="OpenAI Model", default="gpt-3.5-turbo-0613")

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ["oopo_state", "openai_model"]

    def _init_messaging(self):
        if self.oopo_state in [False, "not_initialized"] and self._is_internal():
            self._init_odoobot()
        return super()._init_messaging()

    def _init_odoobot(self):
        self.ensure_one()
        oopo_id = self.env["ir.model.data"]._xmlid_to_res_id("base.partner_root")
        channel_info = self.env["mail.channel"].channel_get([oopo_id, self.partner_id.id])
        channel = self.env["mail.channel"].browse(channel_info["id"])
        message = self.system_prompt
        channel.sudo().message_post(body=message, author_id=oopo_id, message_type="comment", subtype_xmlid="mail.mt_comment")
        self.sudo().oopo_state = "idle"
        return channel
    