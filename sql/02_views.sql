-- View 1: resumo geral das temperaturas
CREATE OR REPLACE VIEW vw_resumo_temperaturas AS
SELECT
MIN(temp) AS temperatura_minima,
MAX(temp) AS temperatura_maxima,
ROUND(AVG(temp), 2) AS temperatura_media,
COUNT(*) AS total_registros
FROM temperature_readings;

-- View 2: resumo por categoria (In/Out)
CREATE OR REPLACE VIEW vw_temperaturas_por_categoria AS
SELECT
out_in AS categoria,
COUNT(*) AS total_registros,
MIN(temp) AS temperatura_minima,
MAX(temp) AS temperatura_maxima,
ROUND(AVG(temp), 2) AS temperatura_media
FROM temperature_readings
GROUP BY out_in;

-- View 3: resumo diário das temperaturas
CREATE OR REPLACE VIEW vw_temperaturas_por_dia AS
SELECT
DATE(noted_date) AS dia,
COUNT(*) AS total_registros,
MIN(temp) AS temperatura_minima,
MAX(temp) AS temperatura_maxima,
ROUND(AVG(temp), 2) AS temperatura_media
FROM temperature_readings
GROUP BY DATE(noted_date);
