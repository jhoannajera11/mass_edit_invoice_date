# -*- coding: utf-8 -*-
from odoo import models, fields

class UpdateInvoiceDateWizard(models.TransientModel):
    _name = 'update.invoice.date.wizard'
    _description = 'Asistente para Actualizar Fecha de Factura'

    invoice_date = fields.Date(string="Nueva Fecha de Factura", required=True)

    def action_update_dates(self):
        active_ids = self.env.context.get('active_ids', [])
        invoices = self.env['account.move'].browse(active_ids)
        invoices.write({'invoice_date': self.invoice_date})
        return {'type': 'ir.actions.act_window_close'}