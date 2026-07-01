from sqlalchemy import create_engine
from config import (
            POSTGRES_USER,
            POSTGRES_PASSWORD,
            POSTGRES_DB,
            POSTGRES_HOST,
            POSTGRES_PORT,
                            )

DATABASE_URL = (
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
            f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
                )

engine = create_engine(DATABASE_URL)
