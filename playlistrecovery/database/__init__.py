from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .playlist import Playlist
from .video import Video
