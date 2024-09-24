# Concerts Management System

This is a Python-based concert management system built with SQLAlchemy, which models the relationship between bands, venues, and concerts. The application tracks which bands are playing in which venues and stores details about the bands' concerts, such as dates and locations. It also includes methods for common operations like fetching the most frequent band at a venue or checking if a concert is a "hometown" show.

## Installation

### Prerequisites

- Python 3.12.5
- SQLAlchemy

### Setup

1. Clone the repository:

```bash
   git clone https://github.com/CGM123sherry/concert_app
   cd concert-app
```

2. Create a virtual environment:

```bash
   pyenv activate phase3env
```

3. Install alembic:

````bash
    alembic init alembic
    ```

3. Install dependencies:

   ```bash
   pip install sqlalchemy
````

4. Set up the SQLite database in the desired directory:

```bash
   sqlite3 app/data/concerts.db
```

5. Run the script to initialize the database:

```bash
   python3 app.py
```

### Database Setup

- The database is an SQLite database stored at `app/data/concerts.db`.
- The models are represented using SQLAlchemy's `declarative_base` model.

## Database Models

### Band Model

The `Band` model represents a musical band with the following fields:

- `id` (Integer): The primary key.
- `name` (String): The name of the band.
- `hometown` (String): The hometown of the band.
- Relationship: A band can have multiple concerts, represented by the `concerts` relationship.

### Venue Model

The `Venue` model represents a concert venue with the following fields:

- `id` (Integer): The primary key.
- `title` (String): The name of the venue.
- `city` (String): The city where the venue is located.
- Relationship: A venue can host multiple concerts, represented by the `concerts` relationship.

### Concert Model

The `Concert` model represents an event where a band performs at a venue on a specific date:

- `id` (Integer): The primary key.
- `band_id` (Foreign Key): Links to the `Band` model.
- `venue_id` (Foreign Key): Links to the `Venue` model.
- `date` (String): The date of the concert.
- Relationships: Each concert is linked to one band and one venue.

## Usage

### Example Data

When you run the script (`app.py`), some sample data is added automatically if the database is empty. For example:

- **Bands:**

  - The Harembe Stars (from Nairobi West)
  - The Lagos Stars (from Lagos)

- **Venues:**

  - Nyayo Stadium (Nairobi)
  - Freedom Park (Accra)

- **Concerts:**
  - The Harembe Stars at Nyayo Stadium (2024-09-20)
  - The Lagos Stars at Freedom Park (2024-10-01)

### How to Use

1. **Running the Script**:
   After setting up the database and adding some sample data, you can run the script:

   ```bash
   python3 app.py
   ```

2. **Interacting with Data**:
   You can interact with the models using SQLAlchemy's ORM methods. For example:

   - **Add a new concert**:

     ```python
     band1.play_in_venue(venue1, "2024-12-25")
     ```

   - **Get all venues where a band has played**:

     ```python
     print(band1.venues())
     ```

   - **Check if a concert is a hometown show**:
     ```python
     print(concert1.hometown_show())
     ```

## Methods

### Band Model Methods

1. `venues()`

   - Returns a list of all venues where the band has performed.

2. `all_introductions()`

   - Returns a list of all introductions the band has given at different concerts.

3. `play_in_venue(venue, date)`

   - Adds a new concert for the band at a specified venue on a given date.

4. `most_performances(session)`
   - Class method that returns the band with the most performances.

### Venue Model Methods

1. `bands()`

   - Returns a list of all bands that have performed at this venue.

2. `concert_on(date)`

   - Returns the concert that took place on a specific date at the venue.

3. `most_frequent_band()`
   - Returns the band that has played most frequently at this venue.

### Concert Model Methods

1. `hometown_show()`

   - Returns `True` if the concert is in the band's hometown, otherwise `False`.

2. `introduction()`
   - Returns the band’s introduction statement for a concert in a specific city.

## Commands

Below are the important commands to run the project.

### Initialize the Database

```bash
python3 app.py
```

This will set up the database and add sample data if it's empty.

### Add a New Band and Venue

You can add new bands, venues, and concerts directly in the script or via an interactive Python shell:

```python
# Create a new band
band = Band(name="The Jazz Masters", hometown="New York")

# Create a new venue
venue = Venue(title="Central Park", city="New York")

# Add a new concert
concert = Concert(band=band, venue=venue, date="2024-12-31")

# Commit to the database
session.add_all([band, venue, concert])
session.commit()
```

### Fetch Band with the Most Performances

```python
top_band = Band.most_performances(session)
print(top_band.name)
```

### Get Concerts for a Venue

```python
venue = session.query(Venue).filter_by(title="Freedom Park").first()
concerts = venue.concerts
for concert in concerts:
    print(concert.introduction())
```

once again here is the repo:
https://github.com/CGM123sherry/concert_app

1. cd concert_app
2. cd app
