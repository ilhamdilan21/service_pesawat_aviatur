from odoo import api, fields, models


class barangdanpelayanan(models.Model):
    _name = 'aviatur.barang'
    _description = 'New Description'

    
    name = fields.Char(string='Nama')
    id_barang= fields.Char(string='ID Barang')
    harga_beli = fields.Integer(string='Harga Beli')
    harga_jual = fields.Integer(string='Harga Jual')
    stok = fields.Integer(string='Stok Barang')
    status = fields.Selection(string='Status Barang', selection=[('empty', 'Empty'), ('available', 'Available'),])
    tanggal_masuk = fields.Date(string='Barang Masuk', required=True)
    tanggal_kadaluarsa = fields.Date(string='Kadaluarsa')
    kodekelompok_id = fields.Many2one(comodel_name='aviatur.kegiatan', 
                                string='Jenis Pelayanan',
                                ondelete='cascade')
