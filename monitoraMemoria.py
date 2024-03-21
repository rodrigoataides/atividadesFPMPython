import time
import psutil

# Obter informações de uso da memória
mem_total = psutil.virtual_memory().total
mem_disponível = psutil.virtual_memory().available

# Formatar a saída
texto_formatado = f"""
**Memória Total:** {mem_total:,} bytes
**Memória Disponível:** {mem_disponível:,} bytes
**Uso da Memória:** {((mem_total - mem_disponível) / mem_total) * 100:.2f}%
"""

# Exibir informações de uso da memória
while True:
    print(texto_formatado)
    time.sleep(1)
