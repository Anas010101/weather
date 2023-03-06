from dotenv import dotenv_values
from sqlalchemy import create_engine

def init(envPath):
      # take environment variables from .env.
      config = dotenv_values(envPath)
      engine = create_engine(
          "mysql://" + config['DB_USERNAME'] + ":" + config['DB_PASSWORD'] + "@" + config['DB_HOSTNAME'] + "/" + config[
              'DB_NAME'], echo=False)
      return engine.connect()