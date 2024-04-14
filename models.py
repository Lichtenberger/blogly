from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    '''Users'''

    __tablename__ = 'users'

    id = db.Column(db.Interger,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.Text,
                           nullable=False,
                           unique=False)
    last_name = db.Column(db.Text,
                          nullable=False,
                          unique=False)
    image_url = db.Column(db.Text,
                          nullable=False,
                          default=DEFAULT_IMAGE_URL)
    
    @property
    def full_name(self):
            '''Users full name'''

            return f"{self.first_name} {self.last_name}"
    
def connect_db(app):
        '''connect database'''

        db.app = app
        db.init_app(app)