from bson import ObjectId
from flask import g, current_app
from flask_validation_extended import Json, Route, Query
from flask_validation_extended import Validator, MinLen
from app.api.response import response_200, created, forbidden, no_content
from app.api.response import bad_request
from app.api.decorator import login_required, timer, admin_required
from app.api.validation import ObjectIdValid
from model.mongodb import Symbol
from . import api_v1 as api

@api.post("symbol/europe/<id>")
@timer
def api_v1_get_washtag_europe():
    pass
@api.post("symbol/korea/<id>")
@timer
def api_v1_get_washtag_korea():
    pass
@api.post("symbol/usa/<id>")
@timer
def api_v1_get_washtag_usa():
    pass
