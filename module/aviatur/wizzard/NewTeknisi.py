from odoo import api, fields, models


class newteknisi(models.TransientModel):
    _name = 'aviatur.newteknisi'
    _description = 'New Description'
    _inherit = 'aviatur.pegawai'

    id_teknisi = fields.Char(string='ID Pegawai')
    status = fields.Selection(string='Status Teknisi', 
            selection=[('junior', 'Junior'),('intern', 'Internship')])
    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    gender = fields.Selection(string='Jenis Kelamin', 
                            selection=[('pria', 'Pria'), ('perempuan', 'Perempuan'),])
    gambar = fields.Image('gambar')
    def button_newteknisi(self):
        for rec in self:
            vals = {
                'id_teknisi': self.id_teknisi,
                'status': self.status,
                'name': self.name,
                'alamat': self.alamat,
                'tgl_lahir': self.tgl_lahir,
                'gender': self.gender,
                'gambar': self.gambar
            }
            print('Data {} berhasil terinput'.format(vals))
            self.env['aviatur.teknisi'].create(vals)
    
