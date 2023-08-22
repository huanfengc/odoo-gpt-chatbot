from odoo import models, fields, api

class MailChannel(models.Model):
    _inherit = "mail.channel"

    first_msg = "Hi, I'm Oopo, an AI assistant. Feel free to ask my any questions."

    def reset_oopo(self):
        self.ensure_one()

        odoobot_id = self.env["ir.model.data"]._xmlid_to_res_id("base.partner_root")

        msgs = self._channel_fetch_message(limit=None)
        msg_ids = [msg["id"] for msg in msgs]
        self.env["mail.message"].browse(msg_ids[0]).write({"body": ""})
        self.env["mail.message"].browse(msg_ids[1:]).unlink()

        message = self.first_msg
        self.sudo().message_post(body=message, author_id=odoobot_id, message_type="comment", subtype_xmlid="mail.mt_comment")
        return False