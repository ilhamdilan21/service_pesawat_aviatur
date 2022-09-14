from odoo import api, fields, models


class pelayanan(models.Model):
    _name = 'aviatur.pelayanan'
    _description = 'New Description'

    name = fields.Char(string='Nama Jasa')
    id_pelayanan= fields.Char(string='ID Pelayanan')
    harga = fields.Integer(string='Harga')
    kodekelompok_id = fields.Many2one(comodel_name='aviatur.kegiatan', 
                                string='Jasa Pelayanan',
                                ondelete='cascade')
