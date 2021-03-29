from flask_app import db
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class Telco(db.Model):
    
    __tablename__ = 'telco'

    id = db.Column(db.Integer)
    tenure = db.Column(db.Integer)
    multi_line = db.Column(db.Integer)
    tech_support = db.Column(db.Integer)
    contract = db.Column(db.Integer)
    pay_method = db.Column(db.String(64))
    paperless_bill = db.Column(db.String(64))
    total_charge = db.Column(db.Float)

    def __init__(self,tenure,multi_line,tech_support,contract,pay_method,paperless_bill,total_charge):
        self.tenure = tenure
        self.multi_line = multi_line
        self.tech_support = tech_support
        self.contract = contract
        self.pay_method = pay_method
        self.paperless_bill = paperless_bill
        self.total_charge = total_charge

    def __repr__(self):
        return f'Customer {self.id}'