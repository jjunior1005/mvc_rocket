# Conexão com o Python no banco de dados em rede
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.pool import NullPool

class DBConnectionHandler:
    def __init__(self) -> None:
        # # self.__connection_string = "sqlite:////mnt/serc_hd/DATASETS/DB_SQLITE/rocket_storage.db"
        # self.__connection_string = "sqlite:///storage.db"
        # self.__engine = None
        # self.session = None
        self.__host  = '192.168.0.4'
        self.__port = '5432'
        self.__database = 'rocket'
        self.__user = 'postgres'
        self.__password = '123456'

        self.__connection_string = (
              f"postgresql://{self.__user}:"
              f"{self.__password}@{self.__host}:"
              f"{self.__port}/{self.__database}"
        )

        self.__engine = None
        self.session = None

    def connect_to_db(self):
        # self.__engine = create_engine(self.__connection_string)
        self.__engine = create_engine(
            self.__connection_string,
            # poolclass=NullPool,
            # pool_size=5,
            # max_overflow=10,
            echo=False
        )

    def get_engine(self):
        return self.__engine
     
    def __enter__(self):
        if not self.__engine:
            self.connect_to_db()
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            if exc_type is not None:
                self.session.rollback()
        self.session.close()
    
db_connection_handler = DBConnectionHandler()    
