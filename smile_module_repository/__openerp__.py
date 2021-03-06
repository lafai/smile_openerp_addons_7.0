# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Smile (<http://www.smile.fr>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Smile Module Repository",
    "version": "0.1",
    "depends": ["product"],
    "author": "Smile",
    "description": """Smile Module Repository

    Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr & bruno.joliveau@smile.fr
    """,
    "summary": "",
    "website": "http://www.smile.fr",
    "category": 'Tools',
    "sequence": 20,
    "init_xml": [
        "security/ir.model.access.csv",
        "security/res_users.yml",
        "data/ir.module.vcs.csv",
        "data/ir.module.version.csv",
        "data/ir.module.repository.tag.csv",
        "data/product.category.csv",
    ],
    "update_xml": [
        "view/ir_module_vcs_view.xml",
        "view/ir_module_version_view.xml",
        "view/ir_module_repository_tag_view.xml",
        "view/ir_module_repository_view.xml",
        "view/product_product_view.xml",
    ],
    'demo_xml': [],
    'test': [],
    "auto_install": False,
    "installable": True,
    "application": False,
}
