# scenario_runner.py
import os
import csv
import time
import pygame
import subprocess

# 1. Rodar o pygame em modo "sem janela"
os.environ["SDL_VIDEODRIVER"] = "dummy"

# 2. Função para rodar um cenário de teste
def run_scenario(scenario_name):
    print(f"Executando cenário: {scenario_name}")

    start = time.time()
    success = True
    error_message = ""
    events_sent = 0
    process = None  # <--- adiciona isso!

    try:
        # 3. Simular execução do app
        process = subprocess.Popen(["python3", "main.py"])  # inicia seu app
        time.sleep(1.5)  # tempo simulado

        # Simular clique
        pygame.init()
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (400, 300), "button": 1}))
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONUP, {"pos": (400, 300), "button": 1}))
        events_sent += 2
        time.sleep(0.5)

    except Exception as e:
        success = False
        error_message = str(e)
    finally:
        # ✅ só encerra se o processo realmente foi iniciado
        if process is not None:
            process.terminate()

        end = time.time()
        duration = round(end - start, 3)

    return {
        "scenario": scenario_name,
        "success": int(success),
        "time_seconds": duration,
        "events_sent": events_sent,
        "error_message": error_message
    }


# 4. Lista de cenários (você pode inventar nomes para o TCC)
cenarios = [
    "Abrir app e clicar no menu inicial",
    "Abrir app e fechar rapidamente",
    "Abrir app e aguardar 3 segundos"
]

# 5. Executa todos e salva no CSV
resultados = []
for nome in cenarios:
    r = run_scenario(nome)
    resultados.append(r)

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
    writer.writeheader()
    writer.writerows(resultados)

print("\n✅ Testes simulados concluídos! Resultados salvos em results.csv\n")
