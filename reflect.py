from sqlalchemy import MetaData, create_engine

engine = create_engine("postgresql://postgres:@localhost:5432/postgres")
metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)

for table in metadata_obj.tables:
    table_obj = metadata_obj.tables[table]
    print(f"Table: {table}")
    for c in table_obj.c:
        print(f"Column: {c.name} Type: {c.type}")
