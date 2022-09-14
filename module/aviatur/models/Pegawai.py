from odoo import api, fields, models
from odoo.exceptions import ValidationError



class Pegawai(models.Model):
    _name = 'aviatur.pegawai'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    gender = fields.Selection(string='Jenis Kelamin', 
                            selection=[('pria', 'Pria'), ('perempuan', 'Perempuan'),])
    gambar = fields.Image('gambar')

    @api.constrains('tgl_lahir')
    def _tanggal_lahir(self):
        if self.tgl_lahir >= self.tgl_lahir.today():
            raise ValidationError('Data Input Salah. Silahkan Ulangi Kembali')

class KepalaTeknisi(models.Model):
    _name = 'aviatur.keptek'
    _description = 'New Description'
    _inherit = 'aviatur.pegawai'

    id_keptek = fields.Char(string='ID Pegawai')
    

    @api.constrains('id_keptek')
    def _check_id_pagawai(self):
        for rec in self:
            ids_keptek = self.env['aviatur.keptek'].search([('id_keptek' , '=', rec.id_keptek), ('id', '!=', rec.id)])
            if ids_keptek:
                raise ValidationError('ID Pegawai {} sudah tersedia'.format(rec.id_keptek))
    
class Teknisi(models.Model):
    _name = 'aviatur.teknisi'
    _description = 'New Description'
    _inherit = 'aviatur.pegawai'

    id_teknisi = fields.Char(string='ID Pegawai')
    status = fields.Selection(string='Status Teknisi', 
            selection=[('junior', 'Junior'), ('senior', 'Senior'), ('intern', 'Internship')])
    

    @api.constrains('id_teknisi')
    def _check_id_pagawai(self):
        for rec in self:
            ids_teknisi = self.env['aviatur.teknisi'].search([('id_teknisi' , '=', rec.id_teknisi), ('id', '!=', rec.id)])
            if ids_teknisi:
                raise ValidationError('ID Pegawai {} sudah tersedia'.format(rec.id_teknisi))

class Penyuci(models.Model):
    _name = 'aviatur.penyuci'
    _description = 'New Description'
    _inherit = 'aviatur.pegawai'

    id_penyuci = fields.Char(string='ID Tukang Cuci')

    @api.constrains('id_penyuci')
    def _constrains_id_penyuci(self):
        for rec in self:
            ids_penyuci = self.env['aviatur.penyuci'].search([('id_penyuci', '=', rec.id_penyuci), ('id', '!=', rec.id)])
            if ids_penyuci:
                raise ValidationError('ID Pegawai {} sudah tersedia'.format(rec.id_penyuci))


class Kasir(models.Model):
    _name = 'aviatur.kasir'
    _description = 'New Description'
    _inherit = 'aviatur.pegawai'

    id_kasir = fields.Char(string='ID Kasir')

    @api.constrains('id_kasir')
    def _constrains_id_kasir(self):
        for rec in self:
            ids_kasir = self.env['aviatur.kasir'].search([('id_kasir', '=', rec.id_kasir), ('id', '!=', rec.id)])
            if ids_kasir:
                raise ValidationError('ID Pegawai {} sudah tersedia'.format(rec.id_penyuci))
    

    
    
    