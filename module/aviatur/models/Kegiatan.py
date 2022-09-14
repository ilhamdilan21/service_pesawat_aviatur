from odoo import api, fields, models


class kegiatan(models.Model):
    _name = 'aviatur.kegiatan'
    _description = 'New Description'

    # name = fields.Char(string='Kode Pelayanan')
    name = fields.Selection([('servicemesin', 'Service Mesin'), 
                ('olimesin', 'Ganti Oli Mesin'),
                ('olirem', 'Ganti Oli Rem'),
                ('sparepart', 'Spare Part'),
                ('cuci_dalam', 'Cuci Bagian Dalam'),
                ('cuci_luar', 'Cuci Bagian Luar'),
                ('jasa', 'Jasa Pemasangan')
                ], string='Nama Pelayanan')

    kode_pelayanan = fields.Char(string='Kode Pelayanan')

    @api.onchange('name')
    def _compute_jenis_pelayanan(self):
        if self.name == 'servicemesin':
            self.kode_pelayanan = 'SM'
        elif self.name =='olimesin':
            self.kode_pelayanan = 'OM'
        elif self.name == 'olirem':
            self.kode_pelayanan = 'OR'
        elif self.name == 'sparepart':
            self.kode_pelayanan = 'SP'
        elif self.name == 'cuci_dalam':
            self.kode_pelayanan = 'Cuci Dalam'
        elif self.name == 'cuci_luar':
            self.kode_pelayanan = 'Cuci Luar'
        elif self.name == 'jasa':
            self.kode_pelayanan = 'Jasa'
            
    pelayanan_ids = fields.One2many(comodel_name='aviatur.barang',
                                    inverse_name='kodekelompok_id',
                                    string='Daftar Barang')
    daftar = fields.Char(string='Daftar Barang atau Pelayanan')
    item = fields.Char(
        compute='_compute_item', string='Item' )
    
    @api.depends('item')
    def _compute_item(self):
        for record in self:
            barang = self.env['aviatur.barang'].search([('kodekelompok_id', '=', record.id)]).mapped('name')
            pelayanan = self.env['aviatur.pelayanan'].search([('kodekelompok_id', '=', record.id)]).mapped('name')
            total_barang = len(barang)
            total_pelayanan = len(pelayanan)
            record.item = total_pelayanan + total_barang 
            record.daftar = pelayanan + barang
    
    status = fields.Selection(string='Status', selection=[('barang', 'Jenis Barang'), ('pelayanan', 'Pelayanan'),])
    