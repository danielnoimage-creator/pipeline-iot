CREATE TABLE IF NOT EXISTS temperature_readings (
    id VARCHAR(100),
    room_id VARCHAR(100),
    noted_date TIMESTAMP,
    temp NUMERIC(6,2),
    out_in VARCHAR(10)
);