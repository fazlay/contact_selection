from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    manufacturer_id = fields.Many2one(
        'res.partner',
        string='Manufacturer',
        domain="[('customer_tag_Type', '=', 'mf')]"
    )
    supplier_id = fields.Many2one(
        'res.partner',
        string='Supplier',
        domain="[('customer_tag_Type', '=', 'sup')]"
    )
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        domain="[('customer_tag_Type', '=', 'cu')]"
    )