# user_simulation.py
import time
import random

def simulate_user(profile: str):
    """
    Simula o comportamento de um usuário baseado em seu perfil.
    Retorna um dicionário com métricas da execução.
    """
    start = time.time()
    events = 0
    errors = 0
    error_message = None

    try:
        if profile == "iniciante":
            for _ in range(random.randint(2, 4)):
                time.sleep(random.uniform(0.8, 1.8))
                events += 1
                # 30% de chance de errar uma ação
                if random.random() < 0.3:
                    errors += 1
                    time.sleep(random.uniform(0.5, 1.0))

        elif profile == "intermediario":
            for _ in range(random.randint(3, 5)):
                time.sleep(random.uniform(0.4, 1.0))
                events += 1
                if random.random() < 0.1:
                    errors += 1
                    time.sleep(random.uniform(0.2, 0.5))

        elif profile == "avancado":
            for _ in range(random.randint(4, 6)):
                time.sleep(random.uniform(0.1, 0.4))
                events += 1
                # quase sem erro
                if random.random() < 0.05:
                    errors += 1
                    time.sleep(random.uniform(0.1, 0.3))
        else:
            raise ValueError(f"Perfil desconhecido: {profile}")

        success = 1 if errors < 3 else 0
        total_time = time.time() - start

        return {
            "profile": profile,
            "success": success,
            "time_seconds": round(total_time, 3),
            "events_sent": events,
            "errors": errors,
            "error_message": error_message
        }

    except Exception as e:
        return {
            "profile": profile,
            "success": 0,
            "time_seconds": 0,
            "events_sent": events,
            "errors": errors,
            "error_message": str(e)
        }
