from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    manufacturer_id = fields.Many2one(
        'res.partner',
        string='Associated Manufacturer',
        domain="[('customer_tag_Type', '=', 'mf')]"
    )
    supplier_id = fields.Many2one(
        'res.partner',
        string='Associated Supplier',
        domain="[('custom_contact_types', '=', 'sup')]"
    )
    customer_id = fields.Many2one(
        'res.partner',
        string='Associated Customer',
        domain="[('custom_contact_types.key', '=', 'cu')]"
    )