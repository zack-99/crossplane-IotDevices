import os
import time
import random
import logging

logging.basicConfig(level=logging.INFO)

class IoTDevice:
    def __init__(self, device_id, interval):
        self.device_id = device_id
        self.interval = interval

    def send_data(self):
        while True:
            value = random.randint(0, 100)
            logging.info(f"Device {self.device_id} sent value: {value}")
            time.sleep(self.interval)

if __name__ == "__main__":
    device_id = os.getenv("DEVICE_ID", "unknown-device")
    interval = int(os.getenv("MESSAGE_INTERVAL", "5"))  # Default 5 sec

    device = IoTDevice(device_id, interval)
    device.send_data()
