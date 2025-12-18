import json
import pandas as pd
import matplotlib.pyplot as plt

with open("newman-report.json") as f:
    data = json.load(f)

executions = data["run"]["executions"]

df = pd.DataFrame([{
    "request": e["item"]["name"],
    "status": e["response"]["status"],
    "code": e["response"]["code"],
    "time_ms": e["response"]["responseTime"],
    "tests_total": len(e["assertions"]),
    "tests_passed": sum(1 for a in e["assertions"] if a["error"] is None),
    "tests_failed": sum(1 for a in e["assertions"] if a["error"] is not None)
} for e in executions])

print("Resumo dos testes:\n", df)

df.plot(x="request", y="time_ms", kind="bar", legend=False)
plt.ylabel("Tempo de resposta (ms)")
plt.title("Performance por requisição")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_tempo_resposta.png")

df[["tests_passed","tests_failed"]].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Taxa de sucesso dos testes")
plt.ylabel("")
plt.savefig("grafico_taxa_sucesso.png")

df["code"].value_counts().plot(kind="bar")
plt.title("Distribuição de Status Codes")
plt.xlabel("Código HTTP")
plt.ylabel("Quantidade")
plt.savefig("grafico_status_codes.png")

df.groupby("request")["time_ms"].mean().plot(kind="bar")
plt.title("Tempo médio de resposta por requisição")
plt.ylabel("ms")
plt.savefig("grafico_tempo_medio.png")

(df["tests_passed"] / df["tests_total"]).plot(kind="bar")
plt.title("Taxa de sucesso por requisição")
plt.ylabel("Proporção")
plt.savefig("grafico_taxa_sucesso_por_request.png")

df.to_csv("resumo_teste.csv", index=False)

