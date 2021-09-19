from playlistrecovery.database import db

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    token = db.Column(db.Text(), nullable=False)
    last_login = db.Column(db.TIMESTAMP, nullable=False)
    last_backup = db.Column(db.TIMESTAMP, nullable=True)

    def __init__(self, user_id, name, email, token, last_login):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.token = token
        self.last_login = last_login
