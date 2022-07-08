# -*- coding: utf-8 -*-

{
    'name': 'WinYourLife eCommerce',
    'category': 'Website/Website',
    'sequence': 50,
    'summary': 'Winimo customizations of eCommerce',
    'website': 'deuse@deuse.be',
    'version': '15.0.1.0.1',
    'description': "",
    'depends': ['website_sale'],
    'data': [
        # 'views/res_partner_views.xml',
        'templates/address.xml',
        'templates/login.xml',
        'templates/checkout.xml',
        # 'templates/payment.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': True,
    'license': 'Other proprietary',
}
