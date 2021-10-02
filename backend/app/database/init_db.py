from datetime import datetime
from pony.orm import Database, db_session, select, set_sql_debug

from app.core.config import settings
from app.models.user import User

NOT_APPLICABLE = "N/A"

def init_db(db: Database) -> None:
    db.generate_mapping(create_tables=True)
    set_sql_debug(settings.SQL_DEBUG=="true")
    # create first superuser
    if settings.FIRST_SUPERUSER:
        with db_session:
            superusers = select(su for su in User
                                if su.email == settings.FIRST_SUPERUSER
                                and su.is_superuser)[:] # Change to User.select
            if len(superusers) == 0:
                superuser = User(
                    email=settings.FIRST_SUPERUSER,
                    password=settings.FIRST_SUPERUSER_PW,
                    phone_no=NOT_APPLICABLE,
                    dob=datetime.now(),
                    is_superuser=True
                )
                superuser_history = superuser.create_history(
                    "create superuser"
                )
