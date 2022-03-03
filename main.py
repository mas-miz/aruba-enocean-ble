#!/usr/bin/env python

import asyncio
import websockets
import sys
import json
import base64
import urllib3
from proto_pb2 import aruba_iot_nb_pb2
from google.protobuf import json_format
from datetime import datetime
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.exceptions import InfluxDBError

#You can generate an API token from the "API Tokens Tab" in the UI
token = "API Token" 
org = "influxdb org name"
bucket = "enocean-ble"

def on_message(message):
    telemetry_str = aruba_iot_nb_pb2.Telemetry()
    telemetry_str.ParseFromString(message)
    telemetry_dict = json_format.MessageToDict(telemetry_str)

    if((('nbTopic', 'telemetry') in telemetry_dict["meta"].items()) == True):
        # create json data for send to influxDB
        ble_json = [{
            "measurement": "enocean-stm-550B",
            "tags": {
                "sensor": "STM 550B",
                "sensor MAC": base64.b64decode(telemetry_dict["reported"][0]["mac"]).hex(),
                "reporter hwType" : telemetry_dict["reporter"]["hwType"],
                "reporter mac" : base64.b64decode(telemetry_dict["reporter"]["mac"]).hex(),
                "reporter ipv4" : telemetry_dict["reporter"]["ipv4"],
                "reporter name" : telemetry_dict["reporter"]["name"],
            },
            "time": datetime.now().astimezone().replace(microsecond=0).isoformat(),
            "fields": {
                "temperature":telemetry_dict["reported"][0]["sensors"]["temperatureC"],
                "illumination":telemetry_dict["reported"][0]["sensors"]["illumination"],
                "humidity":telemetry_dict["reported"][0]["sensors"]["humidity"],
                "contact": telemetry_dict["reported"][0]["sensors"]["contact"][0]["state"],
                "accelerationX": telemetry_dict["reported"][0]["sensors"]["accelerometer"]["x"],
                "accelerationY": telemetry_dict["reported"][0]["sensors"]["accelerometer"]["y"],
                "accelerationZ": telemetry_dict["reported"][0]["sensors"]["accelerometer"]["z"],
            }
        }]

        # write data using influxDB iibrary
        with InfluxDBClient(url="influxdb host url:8086", token=token, org=org) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            try:
                write_api.write(bucket, org, ble_json)
            except InfluxDBError as e:
                print(e)
                # missing credentials
                if e.status == 401:
                    raise Exception(f"Incorrect authentication...") from e
                # badly formatted
                if e.status == 400:
                    message = json.loads(e.body)['message']
                    raise Exception(f"Badly formatted... '{message}'.") from e
                raise
            except urllib3.exceptions.HTTPError as e:
                print(e)
                print("##### InfluxDB HTTPError #####")

            except Exception as e:
                print(e)

            print("##### Send sensor data to InfluxDB #####")

    else: print("##### not send sensor data to InfluxDB #####")

async def handler(websocket, path):
    while True:
        message = await websocket.recv()
        on_message(message)

async def main():
    async with websockets.serve(handler, "", 6666):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
