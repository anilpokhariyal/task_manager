from connection import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import sqlalchemy


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), server_default=sqlalchemy.text("gen_random_uuid()"), primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    role = db.Column(db.String)
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    created_by = db.Column(UUID(as_uuid=True), nullable=True)
