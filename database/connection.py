from config.settings import Settings
from google.cloud import bigquery


def get_connection():
    client = bigquery.Client()
    return client


if __name__ == "__main__":
    client = get_connection()
    print(type(client))    