# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 29, 2025 04:40:07
# Database: sqlite:////tmp/tmp.QbeDwsbLx7-01JJR5PZMJBAW84VGSEW4E4FZR/NFLDataModelSystem/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Fan(Base):  # type: ignore
    """
    description: Represents a fan placing an order for merchandise.
    """
    __tablename__ = 'fan'
    _s_collection_name = 'Fan'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="fan")
    AutographRequestList : Mapped[List["AutographRequest"]] = relationship(back_populates="fan")



class HistoricTeam(Base):  # type: ignore
    """
    description: Contains historical data about teams that have existed in the past.
    """
    __tablename__ = 'historic_team'
    _s_collection_name = 'HistoricTeam'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    date_formed = Column(Date)
    date_ceased = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)



class Merchandise(Base):  # type: ignore
    """
    description: Tracks available marketing merchandise and whether they are autographed.
    """
    __tablename__ = 'merchandise'
    _s_collection_name = 'Merchandise'  # type: ignore

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    is_autographed = Column(Boolean)
    price = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="merchandise")
    SignedMerchandiseList : Mapped[List["SignedMerchandise"]] = relationship(back_populates="merchandise")



class Position(Base):  # type: ignore
    """
    description: Stores data about football player positions.
    """
    __tablename__ = 'position'
    _s_collection_name = 'Position'  # type: ignore

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    season_start = Column(Date)
    season_end = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)
    PlayerList : Mapped[List["Player"]] = relationship(back_populates="position")



class Team(Base):  # type: ignore
    """
    description: Stores information about teams, including name, city, date they were formed, and date they ceased operations.
    """
    __tablename__ = 'team'
    _s_collection_name = 'Team'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    date_formed = Column(Date)
    date_ceased = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)
    PlayerList : Mapped[List["Player"]] = relationship(back_populates="team")



class Order(Base):  # type: ignore
    """
    description: Holds information about orders from fans for merchandise items.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore

    id = Column(Integer, primary_key=True)
    fan_id = Column(ForeignKey('fan.id'), nullable=False)
    merchandise_id = Column(ForeignKey('merchandise.id'), nullable=False)
    order_date = Column(Date)
    quantity = Column(Integer)
    total_price = Column(Float)

    # parent relationships (access parent)
    fan : Mapped["Fan"] = relationship(back_populates=("OrderList"))
    merchandise : Mapped["Merchandise"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)



class Player(Base):  # type: ignore
    """
    description: Stores player information including name, birthdate, position, and team.
    """
    __tablename__ = 'player'
    _s_collection_name = 'Player'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date)
    position_id = Column(ForeignKey('position.id'))
    team_id = Column(ForeignKey('team.id'))

    # parent relationships (access parent)
    position : Mapped["Position"] = relationship(back_populates=("PlayerList"))
    team : Mapped["Team"] = relationship(back_populates=("PlayerList"))

    # child relationships (access children)
    AutographRequestList : Mapped[List["AutographRequest"]] = relationship(back_populates="player")
    BenefitList : Mapped[List["Benefit"]] = relationship(back_populates="player")
    CareerStatList : Mapped[List["CareerStat"]] = relationship(back_populates="player")
    SignedMerchandiseList : Mapped[List["SignedMerchandise"]] = relationship(back_populates="player")
    StatisticList : Mapped[List["Statistic"]] = relationship(back_populates="player")



class AutographRequest(Base):  # type: ignore
    """
    description: Keeps record of autograph requests by fans for specific players.
    """
    __tablename__ = 'autograph_request'
    _s_collection_name = 'AutographRequest'  # type: ignore

    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    fan_id = Column(ForeignKey('fan.id'), nullable=False)

    # parent relationships (access parent)
    fan : Mapped["Fan"] = relationship(back_populates=("AutographRequestList"))
    player : Mapped["Player"] = relationship(back_populates=("AutographRequestList"))

    # child relationships (access children)



class Benefit(Base):  # type: ignore
    """
    description: Tracks potential benefits for each player including medical and financial.
    """
    __tablename__ = 'benefit'
    _s_collection_name = 'Benefit'  # type: ignore

    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    medical = Column(String)
    financial = Column(String)

    # parent relationships (access parent)
    player : Mapped["Player"] = relationship(back_populates=("BenefitList"))

    # child relationships (access children)



class CareerStat(Base):  # type: ignore
    """
    description: Aggregates career statistics for players.
    """
    __tablename__ = 'career_stats'
    _s_collection_name = 'CareerStat'  # type: ignore

    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    total_games = Column(Integer)
    total_touchdowns = Column(Integer)
    average_yards = Column(Float)

    # parent relationships (access parent)
    player : Mapped["Player"] = relationship(back_populates=("CareerStatList"))

    # child relationships (access children)



class SignedMerchandise(Base):  # type: ignore
    """
    description: Records signed merchandise available for fans.
    """
    __tablename__ = 'signed_merchandise'
    _s_collection_name = 'SignedMerchandise'  # type: ignore

    id = Column(Integer, primary_key=True)
    merchandise_id = Column(ForeignKey('merchandise.id'), nullable=False)
    player_id = Column(ForeignKey('player.id'), nullable=False)

    # parent relationships (access parent)
    merchandise : Mapped["Merchandise"] = relationship(back_populates=("SignedMerchandiseList"))
    player : Mapped["Player"] = relationship(back_populates=("SignedMerchandiseList"))

    # child relationships (access children)



class Statistic(Base):  # type: ignore
    """
    description: Records player statistics including games played, touchdowns, and yards.
    """
    __tablename__ = 'statistic'
    _s_collection_name = 'Statistic'  # type: ignore

    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    games_played = Column(Integer)
    touchdowns = Column(Integer)
    yards = Column(Integer)

    # parent relationships (access parent)
    player : Mapped["Player"] = relationship(back_populates=("StatisticList"))

    # child relationships (access children)
