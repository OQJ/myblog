from app import app
from app.model import db, Admin

@app.cli.command()
def init_db():
    db.drop_all()
    db.create_all()


@app.cli.command()
def init_admin():
    admin = Admin.query.first()
    if not admin:
        admin = Admin(name='admin')
        admin.set_password_hash('123456')
    db.session.add(admin)
    db.session.commit()