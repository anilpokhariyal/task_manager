from connection import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import sqlalchemy


class Task(db.Model):
    id = db.Column(UUID(as_uuid=True), server_default=sqlalchemy.text("gen_random_uuid()"), primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    project_id = db.Column(UUID(as_uuid=True), db.ForeignKey('projects.id'), nullable=True)
    label = db.Column(db.String)
    due_date = db.Column(db.Date, nullable=True)
    requirement = db.Column(db.String, nullable=True)
    technical_description = db.Column(db.String, nullable=True)
    test_plan = db.Column(db.String, nullable=True)
    release_notes = db.Column(db.String, nullable=True)
    task_status = db.Column(UUID(as_uuid=True), nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)

    assignee = db.relationship('TaskAssignment', backref='tasks', lazy=True)
