# -*- coding: utf-8 -*-
{
    'name': "aviatur",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/kegiatan_view.xml',
        'views/barang_view.xml',
        'views/pelayanan_view.xml',
        'views/keptek_view.xml',
        'views/pegawai_view.xml',
        'views/teknisi_view.xml',
        'views/tukangcuci_view.xml',
        'views/kasir_view.xml',
        'views/riwayatservice_view.xml',
        'wizzard/newteknisi_wizzard.xml',
        'report/report.xml',
        'report/RiwayatServicepdf.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
