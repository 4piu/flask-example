from shared import db


class User(db.Model):
    __tablename__ = "user"

    # attr
    uuid: bytes = db.Column(db.BINARY(16), primary_key=True)   # PK
    creation_time: int = db.Column(db.Integer, nullable=False)
    email: str = db.Column(db.String(256))
    alias: str = db.Column(db.String(256))
    bio: str = db.Column(db.Text)
    password_salt: bytes = db.Column(db.BINARY(16), nullable=False)
    password_hash: bytes = db.Column(db.BINARY(20), nullable=False)
    role: str = db.Column(db.String(256), default="USER", nullable=False)

    def __repr__(self):
        return f"<User {self.uuid.hex()}: {self.email}>"
