# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models

class Purchase(models.Model):
    _inherit = "purchase.py"

    is_shipped = fields.Boolean(help="True if all picking orders are done or cancelled (computed)")