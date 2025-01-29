import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 3003699522845528894 in succeeded_hashes:  # avoid duplicate inserts
            instance = player1 = Player(id=1, name="John Doe", birthdate=date(1990, 4, 15), position_id=1, team_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3003699522845528894)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5889836482442385935 in succeeded_hashes:  # avoid duplicate inserts
            instance = player2 = Player(id=2, name="Jane Smith", birthdate=date(1992, 8, 22), position_id=2, team_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5889836482442385935)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6963992339433209494 in succeeded_hashes:  # avoid duplicate inserts
            instance = player3 = Player(id=3, name="Jake Williams", birthdate=date(1985, 12, 5), position_id=3, team_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6963992339433209494)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8031530104424423408 in succeeded_hashes:  # avoid duplicate inserts
            instance = player4 = Player(id=4, name="Emily Turner", birthdate=date(1993, 6, 19), position_id=4, team_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8031530104424423408)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8356064378910884976 in succeeded_hashes:  # avoid duplicate inserts
            instance = position1 = Position(id=1, title="Quarterback", season_start=date(2000, 9, 1), season_end=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8356064378910884976)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1532684301198147495 in succeeded_hashes:  # avoid duplicate inserts
            instance = position2 = Position(id=2, title="Wide Receiver", season_start=date(2001, 9, 1), season_end=date(2010, 2, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1532684301198147495)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4777161008255277325 in succeeded_hashes:  # avoid duplicate inserts
            instance = position3 = Position(id=3, title="Linebacker", season_start=date(1999, 9, 1), season_end=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4777161008255277325)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5891743934658299895 in succeeded_hashes:  # avoid duplicate inserts
            instance = position4 = Position(id=4, title="Kicker", season_start=date(2005, 9, 1), season_end=date(2015, 2, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5891743934658299895)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4686831715698559380 in succeeded_hashes:  # avoid duplicate inserts
            instance = team1 = Team(id=1, name="Ravens", city="Baltimore", date_formed=date(1996, 11, 6), date_ceased=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4686831715698559380)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8786069402078450564 in succeeded_hashes:  # avoid duplicate inserts
            instance = team2 = Team(id=2, name="Giants", city="New York", date_formed=date(1925, 8, 1), date_ceased=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8786069402078450564)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3163024812050367472 in succeeded_hashes:  # avoid duplicate inserts
            instance = team3 = Team(id=3, name="Patriots", city="New England", date_formed=date(1959, 11, 16), date_ceased=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3163024812050367472)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5821037255598281765 in succeeded_hashes:  # avoid duplicate inserts
            instance = team4 = Team(id=4, name="Bears", city="Chicago", date_formed=date(1920, 9, 17), date_ceased=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5821037255598281765)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
