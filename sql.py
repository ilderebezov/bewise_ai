import dotenv
import os

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

dotenv.load_dotenv()

engine = create_engine(f"postgresql+psycopg2://{os.environ['db_user']}:{os.environ['db_user_password']}"
                       f"@{os.environ['db_host']}:{os.environ['db_port']}/{os.environ['db_name']}")
session = Session(engine)


def protected_commit():
    """

    Method to create protected commit in data base, in a case troubles during commit
    the will be canceled and there is no any data will be added to data base.
    :return: None

    """

    try:
        session.commit()
        session.close()
    except Exception as error:
        logger.error(str(error))
        session.rollback()
        raise error
