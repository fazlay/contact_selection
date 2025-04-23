from odoo import models, fields

class CustomContactType(models.Model):

    _description = 'Contact Category'
    _inherit = 'res.partner'

    custom_contact_types = fields.Many2one("contact.selection.type")

