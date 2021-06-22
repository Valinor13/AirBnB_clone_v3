from flask import Blueprint
from api.v1.views.index import *
app_views = Blueprint('app_views', __name__,
                      template_folder= templates)

@BNB3_route('/api/v1')
