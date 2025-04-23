# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ContactType(models.Model):
    _name = 'contact.selection.type'
    _description = 'contact-selection-type'

    name = fields.Char(string='Name', required=True)
    key = fields.Char(string='Key', required=True)