{
    "name": "Oopo AI Assistant",
    "summary": "Oopo AI Assistant",
    "description": """AI-Powered Assistant inside Odoo""",
    "version": "1.0.0",
    "category": "Custom Development",
    "license": "OPL-1",
    "depends": ["mail_bot"],
    "data": [
        "views/res_config_settings.xml",
        "views/res_users_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "mail_oopo/static/src/*.js",
            "mail_oopo/static/src/*.xml",
        ],
    },
    "author": "Odoo Inc",
    "website": "www.odoo.com",
    "application": False,
    "installable": True,
}