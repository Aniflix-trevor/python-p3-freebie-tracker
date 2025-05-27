#!/usr/bin/env python3

# Script goes here!
from models import Dev, Company, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Drop and recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create companies
google = Company(name="Google", founding_year=1998)
apple = Company(name="Apple", founding_year=1976)
microsoft = Company(name="Microsoft", founding_year=1975)

# Create devs
alice = Dev(name="Alice")
bob = Dev(name="Bob")

# Give freebies
f1 = Freebie(item_name="T-shirt", value=100, dev=alice, company=google)
f2 = Freebie(item_name="Sticker", value=10, dev=bob, company=apple)
f3 = Freebie(item_name="Mug", value=50, dev=alice, company=google)

session.add_all([google, apple, microsoft, alice, bob, f1, f2, f3])
session.commit()
