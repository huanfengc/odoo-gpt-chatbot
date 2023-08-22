/** @odoo-module **/

import { registerPatch } from '@mail/model/model_core';
import { attr } from '@mail/model/model_field';
import { clear } from '@mail/model/model_field_command';
import { browser } from "@web/core/browser/browser";

registerPatch({
    name: "Thread",
    lifecycleHooks: {
        _created() {
            this.messaging.rpc({
                model: 'mail.bot',
                method: 'get_model',
                args: [0],
            }).then((res) => {
                this.update({selectedGPTModel: res});
            });
        },
    },
    recordMethods: {
        onClickChangeModel(ev) {
            ev.stopPropagation();
            this.messaging.rpc({
                model: 'mail.bot',
                method: 'change_model',
                args: [0,ev.target.value],
            });
            this.update({ selectedGPTModel: ev.target.value });
        }
    },
    fields: {
        isChannelRenamable: {
            compute() {
                if (!this.channel) {
                    return clear();
                }
                return this.channel.displayName !== "OdooBot" && this._super();
            }
        },
        selectedGPTModel: attr({
            default: ''
        }),
    },
})