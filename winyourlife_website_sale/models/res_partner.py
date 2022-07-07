from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    # accept_sale_condition = fields.Boolean("Accept Sale Condition", readonly=True)
