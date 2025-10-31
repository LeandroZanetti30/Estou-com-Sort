# scenario_runner.py
import csv
from datetime import datetime
from user_simulation import simulate_user

def run_user_tests():
    profiles = ["iniciante", "intermediario", "avancado"]
    repetitions = 5  # quantas execuções por perfil

    results = []

    print("🚀 Iniciando testes automatizados de usuário...\n")
    for profile in profiles:
        print(f"Executando perfil: {profile}")
        for i in range(repetitions):
            r = simulate_user(profile)
            r["run"] = i + 1
            r["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            results.append(r)
            print(f"  → Execução {i+1}: tempo={r['time_seconds']}s, erros={r['errors']}, sucesso={r['success']}")

    # salva resultados
    csv_filename = "user_test_results.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Testes de usuário concluídos! Resultados salvos em '{csv_filename}'.")

if __name__ == "__main__":
    run_user_tests()
