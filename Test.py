import os 

print(os.getenv("DATABASE_URL","mysql+pymysql://root:root@localhost:3306/ContactManagerDB"))
