from playlistrecovery.database import db

class Video(db.Model):
    __tablename__ = "video"
    video_id = db.Column(db.String(255), nullable=False)
    playlist_id = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    recovery_time = db.Column(db.TIMESTAMP, nullable=True)
    lost = db.Column(db.Boolean(), nullable=False, server_default=db.false())

    def __init__(self, video_id, playlist_id, title):
        self.video_id = video_id
        self.playlist_id = playlist_id
        self.title = title
