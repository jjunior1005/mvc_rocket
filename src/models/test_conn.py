from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Samba
engine = create_engine('sqlite:////mnt/serc_hd/DATASETS/DB_SQLITE/rocket_storage.db')

# Criar a sessão
Session = sessionmaker(bind=engine)
session = Session()

print(session.is_active)

