from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class RiwayatService(models.Model):
    _name = 'aviatur.riwayatservice'
    _description = 'New Description'

    name = fields.Char(string='Name Customer')
    tgl_masuk = fields.Date(string='Tanggal Pesawat Masuk', default=fields.Datetime.now())
    tgl_selesai = fields.Date(string='Tanggal Pesawat Selesai')
    no_nota = fields.Char(string='No Nota')
    jenis_pswt = fields.Selection(string='Jenis Pesawat', selection=[('boeing', 'Boeing'), ('airbus', 'Airbus'),])
    gambar_pswt = fields.Image(string='Gambar Pesawat')
    total_pembayaran = fields.Integer(string='Total Pembayaran', compute='_compute_total_pembayaran')
    detailonderdil_ids = fields.One2many(comodel_name='aviatur.onderdil', 
                                    inverse_name='onderdil_id', 
                                    string='Detail Onderdil', ondelete='cascade')

    detailjasa_ids = fields.One2many(comodel_name='aviatur.jasa', 
                                    inverse_name='jasa_id', 
                                    string='Detail Jasa', ondelete='cascade')
    state = fields.Selection(string='Status', 
                            selection=[('draft', 'Draft'),
                                        ('confirm', 'Confirm'),
                                        ('done','Done'),
                                        ('cancelled', 'Cancelled'),
                                        ],
                            required=True, readonly=True, default='draft')
    
    def action_confirm(self):
        self.write({'state': 'confirm'})
    
    def action_done(self):
        self.write({'state': 'done'})
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})
    
     
    @api.depends('detailonderdil_ids', 'detailjasa_ids')
    def _compute_total_pembayaran(self):
        for rec in self:
            harga_onderdil = sum(self.env['aviatur.onderdil'].search([('onderdil_id', '=', rec.id)]).mapped('subtotal'))
            harga_jasa = sum(self.env['aviatur.jasa'].search([('jasa_id', '=', rec.id)]).mapped('subtotal'))
            rec.total_pembayaran = harga_onderdil + harga_jasa
    
    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise UserError('Tidak dapat menghapus, status bukan DRAFT')
        else:
            if self.detailonderdil_ids and self.detailjasa_ids:
                dataonderdil = []
                datajasa = []
                for rec in self:
                    dataonderdil = self.env['aviatur.onderdil'].search([('onderdil_id', '=', rec.id)])
                    datajasa = self.env['aviatur.jasa'].search([('jasa_id', '=', rec.id)])
                    print(dataonderdil)
                    print(datajasa)
                for ob1 in dataonderdil:
                    print(str(ob1.barang_id.name)+' '+str(ob1.qty))
                    ob1.barang_id.stok += ob1.qty
        record = super(RiwayatService, self).unlink()
    
    def write(self, vals):
        for rec in self:
            dataonderdil = self.env['aviatur.onderdil'].search([('onderdil_id', '=', rec.id)])
            print(dataonderdil)
            for data in dataonderdil:
                print(str(data.barang_id.name) + ' ' + str(data.qty) + ' ' + str(data.barang_id.stok))
                data.barang_id.stok += data.qty
        record = super(RiwayatService, self).write(vals)
        for rec in self:
            dataonderdil2 = self.env['aviatur.onderdil'].search([('onderdil_id', '=', rec.id)])
            print(dataonderdil)
            print(dataonderdil2)
            for databaru in dataonderdil:
                if databaru in dataonderdil2:
                    print(str(databaru.barang_id.name) + " " + str(databaru.qty) + ' ' + str(databaru.barang_id.stok))
                    databaru.barang_id.stok -= databaru.qty
                else:
                    pass 
        return record

    @api.constrains('no_nota')
    def _check_nota(self):
        for rec in self:
            nota = self.env['aviatur.riwayatservice'].search([('no_nota','=', rec.no_nota), ('id', '!=', rec.id)])
            if nota:
                raise ValidationError('No Nota {} sudah tersedia. Silahkan Ganti ke nomor selanjutnya'.format(rec.no_nota))
            elif rec.name == '' or rec.name == 0:
                raise ValidationError('Data Belum Terinput')

    
    
    
    
    
