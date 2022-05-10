# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CinemaWizard(models.TransientModel):
    _name = 'cinema.wizard'
    currency_id = fields.Many2one(
        'res.currency', string='Currency')

    def _get_default_visitor(self):
        return self.env.uid

    def _get_default_movie_show_id(self):
        return self.env.context.get('active_id', None)

    visitor_id = fields.Many2one(
        'res.partner',
        string='visitor',
        required=True,
        default=_get_default_visitor,
    )
    movie_show_id = fields.Many2one(
        'cinema.movie_show',
        sring='movie show',
        required=True,
        default=_get_default_movie_show_id,
    )
    amount = fields.Integer(
        'amount',
        default=1,
        required=True
    )
    place_category_id = fields.Many2one('cinema.place_category',
                                        string='Place category',
                                        required=True)
    price = fields.Monetary(
        'Ticket price',
        compute='_compute_ticket_price',
        readonly=True,
    )

    @api.depends('movie_show_id', 'amount', 'place_category_id')
    def _compute_ticket_price(self):
        for record in self:
            price = self.env['cinema.tickets_price'].search(
                [('cinema_movie_show_id', '=', record.movie_show_id.id),
                 ('place_category_id', '=', record.place_category_id.id)]).price
            record.price = price * record.amount

    # todo add category of places

    def buy_tickets(self):
        if 'movie_show_id' in self:
            tickets_model = self.env['cinema.ticket']
            list_of_order = [
                {
                    'visitor_id': self.visitor_id.id,
                    'cinema_movie_show_id': self.movie_show_id.id,
                    'place_category_id': self.place_category_id.id,
                    'number': 'New'
                }
                for _ in range(self.amount)
            ]
            tickets_model.create(list_of_order)

            action = {
                'name': 'Your ticket(s) to these movie show',
                'view_mode': 'kanban',
                'res_model': 'cinema.ticket',
                'target': 'current',
                'type': 'ir.actions.act_window',
                'domain': [
                    ('visitor_id', '=', self.visitor_id.id),
                    ('cinema_movie_show_id', '=', self.movie_show_id.id),
                ]}
        return action
