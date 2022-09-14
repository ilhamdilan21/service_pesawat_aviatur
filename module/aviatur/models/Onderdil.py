from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Onderdil(models.Model):
    _name = 'aviatur.onderdil'
    _description = 'New Description'

    name = fields.Char(string='Nama Onderdil')
    onderdil_id = fields.Many2one(comodel_name='aviatur.riwayatservice', string='Detail Onderdil')
    barang_id = fields.Many2one(comodel_name='aviatur.barang', string='List Barang')
    harga_satuan_barang = fields.Integer(string='Harga Satuan Barang')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(string='Subtotal', compute='_compute_subtotal')
    
    
    @api.depends('harga_satuan_barang', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.harga_satuan_barang * rec.qty
    

    @api.onchange('barang_id')
    def _compute_barang_id(self):
        if(self.barang_id.harga_jual):
            self.harga_satuan_barang = self.barang_id.harga_jual
    
    @api.model
    def create(self, vals):
        record = super(Onderdil, self).create(vals)
        if record.qty:
            self.env['aviatur.barang'].search([('id','=',record.barang_id.id)]).write({
                'stok':record.barang_id.stok - record.qty
            })
        return record 

    
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty<1:
                raise ValidationError('Kamu belum memasukan jumlah barang {}. Silahkan cek kembali'.format(rec.barang_id.name))
            elif rec.barang_id.stok < rec.qty:
                raise ValidationError('Barang {} tidak tersedia, barang tinggal {}'.format(rec.barang_id.name, rec.barang_id.stok))
            elif rec.barang_id.stok == 0:
                raise ValidationError('Barang {} sudah habis'.format(rec.barang_id.stok))