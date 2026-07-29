import time
import serial
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# ==========================
# InfluxDB 설정
# ==========================
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "-Fa55Typ6pqYSaPzvpbzWytp81YxZ0UjFYsPA7S0zq64XRgEy4p9BiVRSxowjNSv3otSde6P0jCaj4OzX0HabA=="
INFLUX_ORG = "my-org"
INFLUX_BUCKET = "soundwave"

# ==========================
# 시리얼 포트
# ==========================
seri = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=None)

# ==========================
# InfluxDB Client 생성
# ==========================
client = InfluxDBClient(
    url=INFLUX_URL,
    token=INFLUX_TOKEN,
    org=INFLUX_ORG
)

write_api = client.write_api(write_options=SYNCHRONOUS)

print("InfluxDB Connected")

try:
    while True:
        if seri.in_waiting > 0:
            try:
                content = seri.readline().decode().strip()
                soundwave = float(content)

                point = (
                    Point("soundwave")
                    .tag("sonnonet", "2222")
                    .field("soundwave", soundwave)
                    .time(time.time_ns(), WritePrecision.NS)
                )

                write_api.write(
                    bucket=INFLUX_BUCKET,
                    org=INFLUX_ORG,
                    record=point
                )

                print(f"Saved : {soundwave}")

            except ValueError:
                print("Invalid serial data")
            except Exception as e:
                print(e)

        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")

finally:
    seri.close()
    client.close()
