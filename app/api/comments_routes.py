from flask import Blueprint, request, session, jsonify
from flask_login import current_user, login_required
from ..models import db
from ..models.review import Review
from ..models.user import User
from sqlalchemy.exc import SQLAlchemyError


comments_routes = Blueprint("comments", __name__)