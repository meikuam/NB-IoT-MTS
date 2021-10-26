from sqlalchemy import create_engine
from src.utils import config


engine = create_engine(
    f"postgresql+psycopg2://{config['postgres']['user']}:{config['postgres']['password']}@{config['postgres']['host']}:{config['postgres']['port']}/postgres",
    pool_size=5,
    max_overflow=1
)
