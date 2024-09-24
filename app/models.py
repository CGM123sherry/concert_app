from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine

# Initializing the base class
Base = declarative_base()

# Configuring the database
DATABASE_URL = 'sqlite:///app/data/concerts.db'
 # Create a database engine
engine = create_engine(DATABASE_URL)
# the session maker for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()

# Band model
class Band(Base):
    __tablename__ = "bands"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    # Relationship to concerts
    concerts = relationship('Concert', back_populates='band')

    def venues(self):
        return [concert.venue for concert in self.concerts]

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    def play_in_venue(self, venue, date):
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)
        session.commit()
        return new_concert
    
    @classmethod
    def most_performances(cls, session):
        return session.query(cls).order_by(cls.concerts.count().desc()).first()

# Venue model
class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    # Relationship to concerts
    concerts = relationship('Concert', back_populates='venue')

    def bands(self):
        return [concert.band for concert in self.concerts]

    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        band_count = {}
        for concert in self.concerts:
            if concert.band not in band_count:
                band_count[concert.band] = 1
            else:
                band_count[concert.band] += 1  
        return max(band_count, key=band_count.get)

# Concert model
class Concert(Base):
    __tablename__ = "concerts"

    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey("bands.id"), nullable=False)
    venue_id = Column(Integer, ForeignKey("venues.id"), nullable=False)
    date = Column(String, nullable=False)

    # Relationships
    venue = relationship('Venue', back_populates='concerts')
    band = relationship('Band', back_populates='concerts')

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!! We are {self.band.name} and we are from {self.band.hometown}"



# Example of how to use this setup in another part of your app
if __name__ == '__main__': 

    # Add sample data
    if not session.query(Band).first():
        band1 = Band(name="The Harembe Stars", hometown="Nairobi West")
        band2 = Band(name="The Lagos Stars", hometown="Lagos")

        venue1 = Venue(title="Nyayo Stadium", city="Nairobi")
        venue2 = Venue(title="Freedom Park", city="Accra")

        concert1 = Concert(band=band1, venue=venue1, date="2024-09-20")
        concert2 = Concert(band=band2, venue=venue2, date="2024-10-01")
        
        session.add_all([band1, band2, venue1, venue2, concert1, concert2])
        session.commit()
