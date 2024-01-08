from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    Game.query.delete()
    
    monopoly = Game(name='Monopoly', 
                   description='Get ready for a grueling family game night!')
    tic_tac_toe = Game(name='Tic Tac Toe', description='something xs and os')
    
    db.session.add_all([monopoly, tic_tac_toe])
    db.session.commit()

    # from solution:
    # game = Game(name="Power Grid",
    #             description="supply the most cities with power")
    # db.session.add(game)
    # db.session.commit()
    


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
