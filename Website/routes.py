from flask import Blueprint, render_template, request,redirect, url_for, session, abort
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

bp = Blueprint('routes', __name__)