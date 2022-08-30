from sqlalchemy import create_engine,MetaData 


#engine =create_engine("mysql+pymysql://root:root12345@127.0.0.1:3307/icumulus") //docker BD

engine =create_engine("mysql+pymysql://sql11515979:P15pA9fei5@sql11.freesqldatabase.com:3306/sql11515979")
meta=MetaData()
conn=engine.connect()

