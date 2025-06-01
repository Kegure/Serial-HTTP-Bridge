# Ponte Serial-HTTP - README

## 📌 Visão Geral
Este script Python cria uma ponte entre dispositivos seriais com o Arduino e servidores HTTP. Ele monitora continuamente uma porta serial e envia os dados recebidos para um servidor web através de requisições HTTP POST.

## 🛠 Funcionalidades
- Comunicação serial com taxa de transmissão configurável
- Envio automático de requisições HTTP POST com payload JSON
- Intervalo de verificação configurável

## ⚙️ Requisitos
- Python 3.x
- Pacotes necessários:
  ```bash
  pip install pyserial requests
  ```

## 🔧 Configuração Básica
Modifique estes parâmetros no bloco `__main__`:
```python
serial_port = '/dev/ttyUSB0'  # ou 'COMx' no Windows
baud_rate = 9600             # deve corresponder à taxa do seu dispositivo
server_url = 'http://localhost:8000/api'  # seu endpoint
```

## 🚀 Como Usar
1. Conecte seu dispositivo serial
2. Configure os parâmetros acima
3. Execute o script:
   ```bash
   python ponte_serial_http.py
   ```

## 🔄 Funcionamento
- O script roda continuamente, verificando novos dados a cada 10 segundos (configurável)
- Os dados recebidos são enviados ao servidor como JSON: `{"data": "seus_dados_serial"}`

## 📊 Saída Esperada
- Mensagens de status da conexão
- Log dos dados recebidos
- Códigos de resposta do servidor

## ⚠️ Observações
- Certifique-se que seu dispositivo serial e servidor estão configurados corretamente
- O script espera dados no formato UTF-8 com terminadores de nova linha
- Para personalizações, modifique os métodos da classe `SerialHTTPBridge` conforme suas necessidades
