from playlistrecovery.database import db

class Playlist(db.Model):
    __tablename__ = "playlist"
    playlist_id = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, server_default=db.false())

    def __init__(self, playlist_id, user_id, title):
        self.playlist_id = playlist_id
        self.user_id = user_id
        self.title = title
