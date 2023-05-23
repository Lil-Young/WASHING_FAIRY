from flask import g, current_app
from flask_validation_extended import Json, Route, File
from flask_validation_extended import Validator, MinLen, Ext, MaxFileCount, MaxLen
from bson.objectid import ObjectId
from app.api.response import response_200, created, no_content, conflict
from app.api.response import bad_request
from app.api.decorator import login_required, timer
from app.api.validation import ObjectIdValid
from controller.util import remove_none_value
from controller.file_util import upload_to_s3
from model.mongodb import Washtag
from . import api_v1 as api

@api.post("fragment_washtag/europe/<id>")
@timer
def api_v1_get_washtag_europe():
    
@api.post("fragment_washtag/korea/<id>")
@timer
def api_v1_get_washtag_korea():
    
@api.post("fragment_washtag/usa/<id>")
@timer
def api_v1_get_washtag_usa():
