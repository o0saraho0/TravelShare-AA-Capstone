from flask import Blueprint, request, session, jsonify
from flask_login import current_user, login_required
from ..models import db
from ..models.collection import Collection
from ..models.user import User
from sqlalchemy.exc import SQLAlchemyError
import random


collections_routes = Blueprint("collections", __name__)