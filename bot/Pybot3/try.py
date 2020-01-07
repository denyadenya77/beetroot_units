import sqlalchemy as db

engine = db.create_engine('sqlite:////home/denis/udemy_django/project_1/helloworld/db.sqlite3')
connection = engine.connect()
metadata = db.MetaData()
hola_bottable = db.Table('hola_bottable', metadata, autoload=True, autoload_with=engine)

#Equivalent to 'SELECT * FROM census'
query = db.select([hola_bottable])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()

code = ResultSet[-1][1]
print(code)



























# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import MetaData
# from sqlalchemy.sql import select


# engine = create_engine('sqlite:////home/denis/udemy_django/project_1/helloworld/db.sqlite3', echo=True)
# db_session = sessionmaker(bind=engine)
# conn = engine.connect()

# m = MetaData()
# m.reflect(engine)
# for table in m.tables.values():
#     if table.name == 'hola_bottable':
#         for column in table.c:
#             if column.name == 'code':




    # print(table.name)
    # for column in table.c:
    #     print(column.name)
