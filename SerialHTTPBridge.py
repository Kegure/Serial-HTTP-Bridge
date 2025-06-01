import serial
import requests
import time
import json

class SerialHTTPBridge:
    def __init__(self, serial_port, baud_rate, server_url):
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.server_url = server_url
        self.ser = None

    def connect_serial(self):
        """Conecta a porta serial"""
        self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
        self.ser.flush()
        print(f"Conectado à porta serial {self.serial_port}")

    def read_serial_data(self):
        """Lê dados da porta serial"""
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            print(f"Dado recebido: {line}")
            return line
        return None

    def send_to_server(self, data):
        """Envia dados para o servidor HTTP"""
        payload = {'data': data}
        try:
            response = requests.post(self.server_url, json=payload)
            print(f"Resposta do servidor: {response.status_code}")
            return response
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")
            return None

    def run(self, interval=10):
        """Executa o loop principal"""
        self.connect_serial()
        try:
            while True:
                data = self.read_serial_data()
                if data:
                    self.send_to_server(data)
                time.sleep(interval)
        except KeyboardInterrupt:
            self.ser.close()
            print("Conexão serial fechada")

if __name__ == "__main__":
    bridge = SerialHTTPBridge(
        serial_port='/dev/ttyUSB0',  
        baud_rate=9600,
        server_url='http://localhost:8000/api'
    )
    bridge.run()
