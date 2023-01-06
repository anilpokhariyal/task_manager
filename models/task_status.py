from connection import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import sqlalchemy


class TaskStatus(db.Model):
    id = db.Column(UUID(as_uuid=True), server_default=sqlalchemy.text("gen_random_uuid()"), primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    sort = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
