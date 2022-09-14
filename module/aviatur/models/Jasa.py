from odoo import api, fields, models


class Jasa(models.Model):
    _name = 'aviatur.jasa'
    _description = 'New Description'

    # name = fields.Char(string='Nama')
    jasa_id = fields.Many2one(comodel_name='aviatur.riwayatservice', string='Detail Riwayat', ondelete='cascade')
    pelayanan_id = fields.Many2one(comodel_name='aviatur.pelayanan', string='List Pelayanan', ondelete='cascade')
    harga_pelayanan = fields.Integer(string='Harga Pelayanan')
    subtotal = fields.Integer(string='Subtotal', compute='_compute_subtotal')
    
    
    @api.depends('harga_pelayanan')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.harga_pelayanan
    
    
    @api.onchange('pelayanan_id')
    def _compute_pelayanan_id(self):
        if(self.pelayanan_id.harga):
            self.harga_pelayanan = self.pelayanan_id.harga
    

    
    