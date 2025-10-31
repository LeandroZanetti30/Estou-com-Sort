# analyze_results.py (versão aprimorada e corrigida)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configurações
INPUT_CSV = "results.csv"
OUT_SUMMARY_CSV = "summary.csv"
OUT_PNG = "grafico_tempo_sucesso.png"
OUT_SVG = "grafico_tempo_sucesso.svg"
FIGSIZE = (10, 6)

def main():
    # Lê os resultados brutos
    df = pd.read_csv(INPUT_CSV)

    print("\n=== RESULTADOS (cru) ===")
    print(df)

    # Gera resumo estatístico por cenário
    summary = df.groupby("scenario").agg(
        success_mean=("success", "mean"),
        time_mean=("time_seconds", "mean"),
        time_std=("time_seconds", "std"),
        events_mean=("events_sent", "mean"),
        runs=("scenario", "count")
    ).reset_index()

    # Substitui NaN por 0 (caso só 1 execução)
    summary["time_std"] = summary["time_std"].fillna(0.0)

    # Ordena por tempo médio (opcional)
    summary = summary.sort_values("time_mean", ascending=False).reset_index(drop=True)

    print("\n=== RESUMO AGRUPADO ===")
    print(summary)

    # Salva CSV resumo
    summary.to_csv(OUT_SUMMARY_CSV, index=False)
    print(f"\nResumo salvo em: {OUT_SUMMARY_CSV}")

        # --- Gera gráfico combinado ---
    x = np.arange(len(summary))
    width = 0.6

    fig, ax1 = plt.subplots(figsize=FIGSIZE)

    # Barras: tempo médio
    bars = ax1.bar(
        x,
        summary["time_mean"],
        width,
        yerr=summary["time_std"],
        capsize=6,
        color="#4A90E2",
        label="Tempo médio (s)"
    )

    ax1.set_xlabel("Cenário", fontsize=11)
    ax1.set_ylabel("Tempo médio (s)", color="#4A90E2", fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(summary["scenario"], rotation=30, ha="right", fontsize=10)
    ax1.set_title("Tempo médio por cenário e taxa de sucesso (%)", fontsize=13, pad=15)

    # Adiciona rótulos nas barras
    for rect, val in zip(bars, summary["time_mean"]):
        ax1.annotate(f"{val:.3f}s",
                     xy=(rect.get_x() + rect.get_width() / 2, val),
                     xytext=(0, 6),
                     textcoords="offset points",
                     ha="center", va="bottom", fontsize=9, color="#333")

    # Eixo secundário (sucesso)
    ax2 = ax1.twinx()
    success_pct = summary["success_mean"] * 100.0
    ax2.plot(x, success_pct, color="tab:green", marker="o", linewidth=2, label="Sucesso (%)")
    ax2.set_ylabel("Sucesso (%)", color="tab:green", fontsize=11)
    ax2.set_ylim(0, 110)

    # Rótulos de sucesso
    for xi, pct in zip(x, success_pct):
        ax2.annotate(f"{pct:.0f}%",
                     xy=(xi, pct),
                     xytext=(0, 8),
                     textcoords="offset points",
                     ha="center", va="bottom",
                     fontsize=9, color="tab:green")

    # Legendas abaixo do gráfico
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    fig.legend(
        handles1 + handles2,
        labels1 + labels2,
        loc="lower center",
        ncol=2,
        frameon=False,
        bbox_to_anchor=(0.5, -0.08),
        fontsize=10
    )

    plt.tight_layout(rect=[0, 0.05, 1, 1])  # margem inferior extra
    plt.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
    plt.savefig(OUT_SVG, bbox_inches="tight")
    print(f"Gráfico salvo em: {OUT_PNG} e {OUT_SVG}")

    plt.show()



if __name__ == "__main__":
    main()
