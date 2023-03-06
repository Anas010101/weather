import sys
import re
import os
from datetime import datetime
from utils import init

def ingest(conn):
    total_count = 0
    start_sql = "INSERT INTO `temperature_history`  (city_code, date, maximum, minimum, precipitation) VALUES "
    end_sql = " ON DUPLICATE KEY UPDATE maximum = VALUES(maximum), minimum = VALUES(minimum), precipitation = VALUES(precipitation)"
    sql = start_sql
    for filename in os.listdir(sys.argv[1]):
        filepath = os.path.join(sys.argv[1], filename)
        if os.path.isfile(filepath):
            f = open(filepath, "r")
            Lines = f.readlines()
            count = 0
            for line in Lines:
                count += 1
                if count % 5000 == 0:
                    conn.execute(sql[:-2] + end_sql)
                    sql = start_sql
                row = re.split(r'\t+', line.strip())
                sql += "('" + filename.replace(".txt", "") + "', '" + datetime.strptime(row[0], '%Y%m%d').strftime('%Y-%m-%d') + "', " + row[1] + ", " + row[2] + ", " + row[3] + "), "
            conn.execute(sql[:-2] + end_sql)
            total_count += count
    print("Total {} records are saved.".format(total_count))


conn = init(".env")
ingest(conn)
