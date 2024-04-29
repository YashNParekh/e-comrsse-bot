# from langchain.llms import GooglePalm
# from langchain_community.llms import GooglePalm

from langchain_google_genai import GoogleGenerativeAI


api_key = 'AIzaSyC0JoJUNku6--vCe4iGgHfnT3QIpYBUMmA'

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key, temperature=0.1)


from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
# !pip install langchain langchain-experimental
db_user = "root"
db_password = ""
db_host = "localhost"
db_name = "Laptop_seles"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

# print(db.table_info)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

def ask_and_get_info(take):
    qns1 = db_chain(take)
    print(qns1)
    if qns1 :
        try : 
           return qns1.split(',').split(":").replace('}',"")
        except : 
            return qns1
    else : 
        return ''

# while True:
#     take = input('enter ')
# print(ask_and_get_info('laptop between price 800 to 1000')).split(',').split(":").replace('}',"")


# sql_code = """