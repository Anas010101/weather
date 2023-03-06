from utils import init

def analyse(conn):
    sql = "INSERT INTO `temperature_statistics` SELECT city_code, YEAR(`date`) AS year, " \
          "AVG(CASE WHEN maximum = -9999 THEN 0 ELSE maximum END) / 10.0 AS maximum_average, " \
          "AVG(CASE WHEN minimum = -9999 THEN 0 ELSE minimum END) / 10.0 AS minimum_average, " \
          "SUM(CASE WHEN precipitation = -9999 THEN 0 ELSE precipitation END) / 10.0 AS accumulated_precipitation " \
          "FROM `temperature_history` GROUP BY city_code, YEAR(`date`) ON DUPLICATE KEY UPDATE " \
          "maximum_average = VALUES(maximum_average), " \
          "minimum_average = VALUES(minimum_average), " \
          "accumulated_precipitation = VALUES(accumulated_precipitation)"
    result = conn.execute(sql)
    print("Total {} records are saved.".format(result.rowcount))

conn = init(".env")
analyse(conn)
