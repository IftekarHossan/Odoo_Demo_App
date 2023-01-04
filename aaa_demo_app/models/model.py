
from odoo import fields, models

class demo_app(models.model):
  _name ="demo.app"
  _description="demo_app"

  name=fields.Char(string="name",required=True)
  description=fields.char(string="description",required=True)