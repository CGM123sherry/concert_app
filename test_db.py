from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Band, Venue, Concert

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a band
new_band = Band(name="The Rolling Moss", hometown="Uganda")
session.add(new_band)
session.commit()
print(f"Added band: {new_band.name}")
