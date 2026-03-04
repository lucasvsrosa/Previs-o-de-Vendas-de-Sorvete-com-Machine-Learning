import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
import os

def train_model():
    # 1. Carregar dados
    data_path = 'inputs/vendas_sorvete.csv'
    if not os.path.exists(data_path):
        print(f"Erro: Arquivo {data_path} não encontrado.")
        return
    
    df = pd.read_csv(data_path)
    X = df[['temperatura']]
    y = df['vendas']

    # 2. Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Iniciar experimento MLflow
    mlflow.set_experiment("Previsao_Vendas_Sorvete")

    with mlflow.start_run():
        # 4. Treinar modelo
        model = LinearRegression()
        model.fit(X_train, y_train)

        # 5. Fazer previsões
        y_pred = model.predict(X_test)

        # 6. Calcular métricas
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"MSE: {mse:.2f}")
        print(f"R2 Score: {r2:.2f}")

        # 7. Logar parâmetros e métricas no MLflow
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)

        # 8. Salvar o modelo no MLflow
        mlflow.sklearn.log_model(model, "modelo_vendas_sorvete")

        # 9. Gerar e salvar gráfico de resultados
        plt.figure(figsize=(10, 6))
        plt.scatter(X, y, color='blue', label='Dados Reais')
        plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linha de Regressão')
        plt.title('Temperatura vs Vendas de Sorvete')
        plt.xlabel('Temperatura (°C)')
        plt.ylabel('Vendas (Quantidade)')
        plt.legend()
        plt.grid(True)
        
        # Salvar gráfico localmente para o README
        plot_path = "outputs/resultado_regressao.png"
        plt.savefig(plot_path)
        print(f"Gráfico salvo em: {plot_path}")
        
        # Logar gráfico como artefato no MLflow
        mlflow.log_artifact(plot_path)

        print("Treinamento concluído e registrado no MLflow com sucesso!")

if __name__ == "__main__":
    # Garantir que a pasta outputs existe
    os.makedirs('outputs', exist_ok=True)
    train_model()
