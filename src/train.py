import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

# Carregar dados
df = pd.read_csv("data/vendas_sorvete.csv")

X = df[["temperatura"]]
y = df["vendas"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Iniciar MLflow
mlflow.start_run()

model = LinearRegression()
model.fit(X_train, y_train)

# Avaliar modelo
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"MSE: {mse:.2f}")

# Log com MLflow
mlflow.log_metric("mse", mse)
mlflow.sklearn.log_model(model, "modelo_regressao")

mlflow.end_run()

print("Treinamento concluído e modelo registrado no MLflow!")
