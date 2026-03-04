import mlflow
import pandas as pd

# Carregar modelo registrado
model = mlflow.sklearn.load_model("mlruns/0/<run_id>/artifacts/modelo_regressao")  # substitua <run_id>

def prever(temperatura):
    return model.predict([[temperatura]])

# Exemplo de previsão
temp = 30
vendas_previstas = prever(temp)
print(f"Temperatura: {temp}°C -> Vendas previstas: {int(vendas_previstas[0])}")
