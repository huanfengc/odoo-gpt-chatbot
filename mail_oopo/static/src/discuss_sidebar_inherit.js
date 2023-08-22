/** @odoo-module **/

import { registerPatch } from '@mail/model/model_core';
import { attr } from '@mail/model/model_field';
import { clear } from '@mail/model/model_field_command';

registerPatch({
    name: "DiscussSidebarCategoryItem",
    fields: {
        hasClearCommand: attr({
            compute() {
                return this.channel.displayName == "OdooBot"
            }
        }),
        hasUnpinCommand: {
            compute() {
                return this.channel.displayName !== "OdooBot" && this._super();
            }
        },
    },
    recordMethods: {
        async onClickClearConversation(ev) {
            ev.stopPropagation();
            await this.messaging.rpc({
                model: 'mail.channel',
                method: 'reset_oopo',
                args: [this.channel.id],
            });
            this.channel.thread.update({ messages: [] });
        }
    }
})