from odoo import http, models, fields
from odoo.http import request
import json


class Barang(http.Controller):
    @http.route('/aviatur/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['aviatur,barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'name': bb.name,
                'id_barang':bb.id_barang,
                'harga_beli':bb.harga_beli,
                'harga_jual':bb.harga_jual,
                'stok':bb.stok,
                'status':bb.status,
                'tanggal_masuk':bb.tanggal_masuk,
                'tanggal_kadaluarsa':bb.tanggal_kadaluarsa
            })
        return json.dumps(isi)