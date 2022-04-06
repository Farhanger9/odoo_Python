# -*- coding: utf-8 -*-

import datetime
from odoo import fields, models, api, _


class SaleProspect(models.Model):
    _name = 'sale.prospect.partner'

    name = fields.Char(string="Name")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', tracking=True)
    