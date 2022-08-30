from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta


demo =Table(
    'demo',meta,
    Column('time',Integer,nullable=False),
    Column('speed',Integer,nullable=False),
    Column('mode_fonctionnement',Integer,nullable=False)

)

