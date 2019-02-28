# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class music_management(models.Model):
#     _name = 'music_management.music_management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class artista(models.Model):
    _name = 'music_management.artista'
    _rec_name ="nombre"
    nombre = fields.Char(string="Nombre",required=True)
    descripcion = fields.Char(string="Descripcion del artista",required=True)
    genero_id = fields.Many2one('music_management.genero',string="Genero")
    album_id = fields.One2many('music_management.album','artista_id',string="Albums del artista")
    comision = fields.Float(string="Comision por cancion",required=True)
    visitas = fields.Integer(string="Numero de visitas", compute="visitas_totales",store=False)
    imagen = fields.Binary()

    @api.one
    @api.depends('visitas')
    def visitas_totales(self):
        for i in self.album_id:
            self.visitas = self.visitas + i.visitas

class album(models.Model):
    _name = 'music_management.album'
    _rec_name = "nombre"
    nombre = fields.Char(string="Nombre",required=True)
    artista_id = fields.Many2one('music_management.artista',string="Artista")
    año = fields.Date(string="Fecha de lanzamiendo", required=True)
    visitas = fields.Integer(string="Numero de visitas",compute='visitas_totales',store=False)
    genero_id = fields.Many2one('music_management.genero',string="Genero")
    cancion_id = fields.One2many('music_management.cancion','album_id',string="Canciones del album")
    imagen = fields.Binary()

    @api.one
    @api.depends('visitas')
    def visitas_totales(self):
        for i in self.cancion_id:
            self.visitas = self.visitas + i.visitas

class cancion(models.Model):
    _name = 'music_management.cancion'

    nombre = fields.Char(string="Nombre de la cancion",required=True)
    año = fields.Date(string="Fecha de lanzamiento", required=True)
    album_id = fields.Many2one('music_management.album',string="Album")
    genero_id = fields.Many2one('music_management.genero',string="Genero")
    visitas = fields.Integer(string="Numero de visitas",required = False)

class genero(models.Model):
    _name = 'music_management.genero'
    _rec_name = "nombre"
    nombre = fields.Char(string="Genero musical", required=True)

class usuario(models.Model):
    _name = 'music_management.usuario'

    nombre = fields.Char(string="Nombre de Usuario",required=True)
    subscripcion = fields.Selection([('F','Gratuita'),('P','Premium'),('P+', 'Premium+')])
    generoMasEscuchado = fields.Many2one('music_management.genero',string="Genero mas Escuchado")
