from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
import uuid #for unique id's
from datetime import datetime
from django.db.models import Max

User = get_user_model()