# -*- coding: utf-8 -*-
from odoo import models,fields


class Actress(models.Model):
  
    _name="sinergy_actress.actress"
    _description="sinergy_actress_actress"
    
      name=fields.Char(string="Nombre")
      height=fields.Char(string="Estatura")
      nationality=fields.Char(string="Nacionalidad")
    
