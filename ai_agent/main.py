import time
from eth_account import Account
from web3 import Web3

class AIAgent:
    def __init__(self, name):
        self.name = name
        # Genera una clave criptográfica privada y una dirección pública de forma nativa (su DNI cripto)
        self.account = Account.create()
        print(f"🤖 [IA] Agente '{self.name}' inicializado.")
        print(f"🔑 Dirección Pública (Identidad): {self.account.address}")

    def execute_and_sign_operation(self, operation_details):
        print(f"⚡ [IA] Ejecutando operación: {operation_details}")
        timestamp = int(time.time())
        
        # Estructuramos el mensaje de la operación
        message_text = f"Agent:{self.name}|Op:{operation_details}|Time:{timestamp}"
        
        # CORRECCIÓN: Usamos encode_defunct para preparar el texto según el estándar EIP-191
        from eth_account.messages import encode_defunct
        signable_message = encode_defunct(text=message_text)
        
        # Firmamos criptográficamente el objeto estructurado
        signed_message = Account.sign_message(signable_message, self.account.key)
        
        print(f"✍️ Firma criptográfica generada con éxito.")
        return {
            "message": message_text,
            "signature": signed_message.signature.hex()
        }


if __name__ == "__main__":
    # Inicialización de prueba simulando 3 tareas del Bot DeFi
    print("=" * 50)
    my_bot = AIAgent("Monad-DeFi-Audit-Bot")
    print("=" * 50)
    
    operaciones = ["Auditar Pool MON/USDT", "Verificar Liquidez de Préstamos", "Validar Oráculo de Precios"]
    for op in operaciones:
        resultado = my_bot.execute_and_sign_operation(op)
        print(f"Firma Única: {resultado['signature'][:40]}...")
        print("-" * 50)
        time.sleep(1)
