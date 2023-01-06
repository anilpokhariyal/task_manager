from connection import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import sqlalchemy


class TimeLog(db.Model):
    id = db.Column(UUID(as_uuid=True), server_default=sqlalchemy.text("gen_random_uuid()"), primary_key=True)
    task_id = db.Column(UUID(as_uuid=True), db.ForeignKey('tasks.id'), nullable=True)
    worked_by = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)
    time = db.Column(db.Integer, server_default=0, comment="In minutes")
    details = db.Column(db.String(255), nullable=True)
    logged_at = db.Column(db.DateTime, server_default=func.now())
    logged_by = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)
