# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Player(Base):
    """description: Stores player information including name, birthdate, position, and team."""
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date)
    position_id = Column(Integer, ForeignKey('position.id'))
    team_id = Column(Integer, ForeignKey('team.id'))

class Position(Base):
    """description: Stores data about football player positions."""
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    season_start = Column(Date)
    season_end = Column(Date)

class Team(Base):
    """description: Stores information about teams, including name, city, date they were formed, and date they ceased operations."""
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String)
    date_formed = Column(Date)
    date_ceased = Column(Date)

class Statistic(Base):
    """description: Records player statistics including games played, touchdowns, and yards."""
    __tablename__ = 'statistic'
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    games_played = Column(Integer)
    touchdowns = Column(Integer)
    yards = Column(Integer)

class Benefit(Base):
    """description: Tracks potential benefits for each player including medical and financial."""
    __tablename__ = 'benefit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    medical = Column(String)
    financial = Column(String)

class Merchandise(Base):
    """description: Tracks available marketing merchandise and whether they are autographed."""
    __tablename__ = 'merchandise'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String, nullable=False)
    is_autographed = Column(Boolean)
    price = Column(Float)

class Order(Base):
    """description: Holds information about orders from fans for merchandise items."""
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fan_id = Column(Integer, ForeignKey('fan.id'), nullable=False)
    merchandise_id = Column(Integer, ForeignKey('merchandise.id'), nullable
        =False)
    order_date = Column(Date)
    quantity = Column(Integer)
    total_price = Column(Float)

class Fan(Base):
    """description: Represents a fan placing an order for merchandise."""
    __tablename__ = 'fan'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)
    address = Column(String)

class AutographRequest(Base):
    """description: Keeps record of autograph requests by fans for specific players."""
    __tablename__ = 'autograph_request'
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    fan_id = Column(Integer, ForeignKey('fan.id'), nullable=False)

class HistoricTeam(Base):
    """description: Contains historical data about teams that have existed in the past."""
    __tablename__ = 'historic_team'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String)
    date_formed = Column(Date)
    date_ceased = Column(Date)

class CareerStats(Base):
    """description: Aggregates career statistics for players."""
    __tablename__ = 'career_stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    total_games = Column(Integer)
    total_touchdowns = Column(Integer)
    average_yards = Column(Float)

class SignedMerchandise(Base):
    """description: Records signed merchandise available for fans."""
    __tablename__ = 'signed_merchandise'
    id = Column(Integer, primary_key=True, autoincrement=True)
    merchandise_id = Column(Integer, ForeignKey('merchandise.id'), nullable
        =False)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    player1 = Player(id=1, name="John Doe", birthdate=date(1990, 4, 15), position_id=1, team_id=1)
    player2 = Player(id=2, name="Jane Smith", birthdate=date(1992, 8, 22), position_id=2, team_id=2)
    player3 = Player(id=3, name="Jake Williams", birthdate=date(1985, 12, 5), position_id=3, team_id=3)
    player4 = Player(id=4, name="Emily Turner", birthdate=date(1993, 6, 19), position_id=4, team_id=4)
    position1 = Position(id=1, title="Quarterback", season_start=date(2000, 9, 1), season_end=None)
    position2 = Position(id=2, title="Wide Receiver", season_start=date(2001, 9, 1), season_end=date(2010, 2, 1))
    position3 = Position(id=3, title="Linebacker", season_start=date(1999, 9, 1), season_end=None)
    position4 = Position(id=4, title="Kicker", season_start=date(2005, 9, 1), season_end=date(2015, 2, 1))
    team1 = Team(id=1, name="Ravens", city="Baltimore", date_formed=date(1996, 11, 6), date_ceased=None)
    team2 = Team(id=2, name="Giants", city="New York", date_formed=date(1925, 8, 1), date_ceased=None)
    team3 = Team(id=3, name="Patriots", city="New England", date_formed=date(1959, 11, 16), date_ceased=None)
    team4 = Team(id=4, name="Bears", city="Chicago", date_formed=date(1920, 9, 17), date_ceased=None)
    
    
    
    session.add_all([player1, player2, player3, player4, position1, position2, position3, position4, team1, team2, team3, team4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
