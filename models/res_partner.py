from odoo import fields, models, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    customer_tag_Type=fields.Selection(selection=[('mf','Manufacturer'),('sup','Supplier'),('cu','Customer')],string="Contact Type")