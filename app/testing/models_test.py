import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Band, Venue, Concert

# Configuring an in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope='module')
def test_session():
    # Create the in-memory database
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()

def test_create_band(test_session):
    # Create and add a band
    band = Band(name="Test Band", hometown="Test Town")
    test_session.add(band)
    test_session.commit()

    # Retrieve band and assert properties
    retrieved_band = test_session.query(Band).filter_by(name="Test Band").first()
    assert retrieved_band is not None
    assert retrieved_band.hometown == "Test Town"

def test_create_venue(test_session):
    # Create and add a venue
    venue = Venue(title="Test Venue", city="Test City")
    test_session.add(venue)
    test_session.commit()

    # Retrieve venue and assert properties
    retrieved_venue = test_session.query(Venue).filter_by(title="Test Venue").first()
    assert retrieved_venue is not None
    assert retrieved_venue.city == "Test City"

def test_create_concert(test_session):
    # Create a band and a venue for the concert
    band = Band(name="Test Band", hometown="Test Town")
    venue = Venue(title="Test Venue", city="Test City")
    test_session.add_all([band, venue])
    test_session.commit()

    # Create and add a concert
    concert = Concert(band=band, venue=venue, date="2024-09-24")
    test_session.add(concert)
    test_session.commit()

    # Retrieve concert and assert relationships
    retrieved_concert = test_session.query(Concert).first()
    assert retrieved_concert is not None
    assert retrieved_concert.band == band
    assert retrieved_concert.venue == venue

def test_hometown_show(test_session):
    # Create a band and venue in the same city (for hometown show)
    band = Band(name="Band Hometown", hometown="Hometown City")
    venue = Venue(title="Venue Hometown", city="Hometown City")
    test_session.add_all([band, venue])
    test_session.commit()

    concert = Concert(band=band, venue=venue, date="2024-11-11")
    test_session.add(concert)
    test_session.commit()

    # Assert that it's a hometown show
    assert concert.hometown_show() == True




