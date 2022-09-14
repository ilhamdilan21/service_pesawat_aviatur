from odoo import api, fields, models


class RiwayatServiceXlsx(models.AbstractModel):
    _name = 'report.aviatur.report_riwayatservice_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'New Description'

    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, barang):
        sheet = workbook.add_worksheet('Daftar Riwayat Transaksi')
        bold = workbook.add_format({'bold':True})
        # sheet.write(0,0,)

        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'No Nota')
        sheet.write(1, 1, 'Nama Pelanggan')
        sheet.write(1, 2, 'Jenis Pesawat')
        sheet.write(1, 3, 'Total yang Dibayarkan')
        sheet.write(1, 4, 'Onderdil dan Jasa')
        row = 2
        col = 0
        for obj in barang:
            col = 0
            sheet.write(row, col, obj.no_nota)
            sheet.write(row, col+1, obj.name)
            sheet.write(row, col+2, obj.jenis_pswt)
            sheet.write(row, col+3, obj.total_pembayaran)
            for obj2 in obj.detailonderdil_ids:
                sheet.write(row, col+4, obj2.barang_id.name)
                col += 1
            for obj3 in obj.detailjasa_ids:
                sheet.write(row, col+5, obj3.pelayanan_id.name)
                col += 1
            row +=1