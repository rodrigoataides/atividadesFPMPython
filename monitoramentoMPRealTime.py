import psutil
import time

# Função para formatar a saída de memória
def formatar_memoria(mem_total, mem_disponível, uso_mem):
    return f"""
**Memória Total:** {mem_total:,} bytes
**Memória Disponível:** {mem_disponível:,} bytes
**Uso da Memória:** {uso_mem:.2f}%
"""

# Função para obter os processos na fila de processamento
def obter_processos_na_fila():
    processos = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent"]):
        try:
            # Obter informações do processo
            pid = proc.info["pid"]
            nome = proc.info["name"]
            uso_cpu = proc.info["cpu_percent"]

            # Adicionar processo à lista
            if uso_cpu > 0.00:
                processos.append((pid, nome, uso_cpu))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processos

# Loop principal
while True:
    # Obter informações de memória
    mem_total = psutil.virtual_memory().total
    mem_disponível = psutil.virtual_memory().available
    uso_mem = ((mem_total - mem_disponível) / mem_total) * 100

    # Obter processos na fila de processamento
    processos_na_fila = obter_processos_na_fila()

    # Exibir informações
    print("Processos na fila de processamento:")
    for processo in processos_na_fila:
        print(f"PID: {processo[0]} - Nome: {processo[1]} - Uso CPU: {processo[2]:.2f}%")

    print(formatar_memoria(mem_total, mem_disponível, uso_mem))
    # Aguardar 3 segundo
    time.sleep(3)
    
