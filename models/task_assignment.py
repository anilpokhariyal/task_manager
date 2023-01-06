from connection import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import sqlalchemy


class TaskAssignment(db.Model):
    id = db.Column(UUID(as_uuid=True), server_default=sqlalchemy.text("gen_random_uuid()"), primary_key=True)
    task_id = db.Column(UUID(as_uuid=True), db.ForeignKey('tasks.id'), nullable=True)
    assigned_to = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)
    time_estimation = db.Column(db.Integer, server_default=0, comment="Time in minutes")
    status = db.Column(db.Integer, server_default=1)
    assigned_at = db.Column(db.DateTime, server_default=func.now())
    assigned_by = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)
