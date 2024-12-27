# -*- coding: utf-8 -*-
# Part of Softhealer Technologies

{
    "name": "Inventory Backdate | Change Effective Date | Backdate In Inventory | Stock Backdate | Warehouse Backdate | Stock Force Date | Inventory Force Date",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Warehouse",
    "summary": "Backdate Remarks incoming order backdate delivery order backdate internal transfer backdate receipt Backdate Mass Confirmation Mass Backdate Force Date in Stock Transfer force date stock picking force date receipt force date shipment Odoo Inventory Adjustment Force Date Change effective date change effective dates effective date changes in effective date effective date change stock effective date change inventory effective date change in stock effective date change in inventory effective date change stock move effective date change product move effective date change incoming order effective date change delivery order effective date change internal transfer",
    "description": """This module is useful for done picking orders (incoming order / delivery order / internal transfer), inventory adjustment and scrap orders with selected backdate. You can put a custom backdate and remarks in the picking & scrap orders. You can mass assign backdate in one click. When you mass assign backdate, it asks for remarks in the mass assign wizard. This selected date and remarks are also reflects in the stock moves & product moves.""",
    "version": "0.0.2",
    "depends": ["stock"],
    "data": [
        'security/ir.model.access.csv',
        'security/sh_stock_backdate_groups.xml',
        'data/stock_picking_data.xml',
        'data/stock_scrap_data.xml',
        'wizard/sh_picking_backdate_wizard_views.xml',
        'wizard/sh_scrap_backdate_wizard_views.xml',
        'views/res_config_settings_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_move_views.xml',
        'views/stock_scrap_views.xml',
        'views/stock_move_line_views.xml',
    ],

    "auto_install": False,
    "installable": True,
    "application": True,
    "images": ["static/description/background.png"],
    "license": "OPL-1",
    "price": 20,
    "currency": "EUR"
}
