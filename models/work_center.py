from odoo import models, fields, api


class CalculateCoast(models.Model):
    _inherit = 'mrp.workcenter'

    op_cost = fields.Float(string='Operational Cost', store=True)
    lab_cost = fields.Float(string='Labour Cost', store=True)
    dep_cost = fields.Float(string='Depreciation Cost', store=True)
    pro_cost = fields.Float(string='Production Cost', store=True)
    other_cost = fields.Float(string='Other Cost', store=True)
    costs_hour = fields.Float(string='Cost per hour',compute='_compute_costs_hour', store=True,readonly=True)
    analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    @api.depends('op_cost','lab_cost','dep_cost','pro_cost','other_cost','costs_hour')
    def _compute_costs_hour (self):
        print("executed")
        self.ensure_one()
        for rec in self:
            if rec.op_cost and rec.dep_cost and rec.pro_cost and rec.lab_cost and rec.other_cost:
                rec.costs_hour = rec.op_cost + rec.dep_cost + rec.lab_cost + rec.pro_cost+rec.other_cost
                print("Done......",rec.costs_hour)
