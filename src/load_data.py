
import pandas as pd
from sqlalchemy import create_engine

CSV_FILE = "data/IOT-temp.csv"

DATABASE_URL = "postgresql+psycopg2://iot_user:iot_password@localhost:5432/iot_database"

print("Lendo dataset...")

df = pd.read_csv(CSV_FILE)

print(f"Registros encontrados: {len(df)}")

df = df.rename(columns={
    "room_id/id": "room_id",
    "out/in": "out_in"
})

df["noted_date"] = pd.to_datetime(
    df["noted_date"],
    format="%d-%m-%Y %H:%M",
    errors="coerce"
)

df["temp"] = pd.to_numeric(df["temp"], errors="coerce")

df = df.dropna(
    subset=["id", "room_id", "noted_date", "temp", "out_in"]
)

print(f"Registros após remover valores nulos: {len(df)}")

duplicados = df.duplicated(subset=["id"]).sum()
print(f"IDs duplicados encontrados: {duplicados}")

df = df.drop_duplicates(subset=["id"], keep="first")

print(f"Registros após remover duplicatas: {len(df)}")

engine = create_engine(DATABASE_URL)

print("Enviando dados para PostgreSQL...")

df.to_sql(
    "temperature_readings",
    engine,
    if_exists="replace",
    index=False,
    chunksize=5000
)

print("Dados carregados com sucesso!")