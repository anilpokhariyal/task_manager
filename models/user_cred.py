from connection import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import sqlalchemy


class UserCred(db.Model):
    id = db.Column(UUID(as_uuid=True), server_default=sqlalchemy.text("gen_random_uuid()"), primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    verification_code = db.Column(db.String)
    verification_status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
