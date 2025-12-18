import json
import pandas as pd
import matplotlib.pyplot as plt

with open("newman-report.json") as f:
    data = json.load(f)

executions = data.get("run", {}).get("executions", [])

rows = []
for e in executions:
    item = e.get("item", {})
    resp = e.get("response", {}) or {}

    assertions = e.get("assertions", []) or []
    tests_total = len(assertions)
    tests_failed = sum(1 for a in assertions if a.get("error") is not None)
    tests_passed = tests_total - tests_failed

    rows.append({
        "request": item.get("name", "sem-nome"),
        "status": resp.get("status", "sem-status"),
        "code": resp.get("code", 0),
        "time_ms": resp.get("responseTime", 0),
        "tests_total": tests_total,
        "tests_passed": tests_passed,
        "tests_failed": tests_failed
    })

df = pd.DataFrame(rows)

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
plt.tight_layout()
plt.savefig("grafico_status_codes.png")

df.groupby("request")["time_ms"].mean().plot(kind="bar")
plt.title("Tempo médio de resposta por requisição")
plt.ylabel("ms")
plt.tight_layout()
plt.savefig("grafico_tempo_medio.png")

taxa = (df["tests_passed"] / df["tests_total"]).fillna(0)
taxa.index = df["request"]
taxa.plot(kind="bar")
plt.title("Taxa de sucesso por requisição")
plt.ylabel("Proporção")
plt.tight_layout()
plt.savefig("grafico_taxa_sucesso_por_request.png")

df.to_csv("resumo_teste.csv", index=False)

