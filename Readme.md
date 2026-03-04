# 🍦 Gelato Mágico - Previsão de Vendas com Machine Learning

## 📌 Sobre o Projeto

Este projeto tem como objetivo desenvolver um modelo de **Machine Learning** capaz de prever a quantidade de sorvetes vendidos com base na temperatura do dia.

A solução foi criada simulando um cenário real de negócio da sorveteria **Gelato Mágico**, onde a previsão correta da demanda pode reduzir desperdícios e maximizar lucros.

---

## 🎯 Objetivos

✔️ Treinar um modelo de regressão para prever vendas
✔️ Avaliar métricas de desempenho
✔️ Registrar experimentos utilizando MLflow
✔️ Estruturar um pipeline reprodutível
✔️ (Opcional) Preparar para deploy em ambiente cloud

---

## 📊 Base de Dados

O dataset contém duas variáveis principais:

* **temperatura (°C)** → variável independente
* **vendas (quantidade de sorvetes vendidos)** → variável dependente

Exemplo:

| Temperatura | Vendas |
| ----------- | ------ |
| 22          | 150    |
| 25          | 200    |
| 30          | 320    |
| 18          | 90     |
| 35          | 400    |

Foi utilizada geração de dados sintéticos para simular cenários reais de venda.

---

## 🧠 Modelagem

Foi utilizado um modelo de **Regressão Linear**, pois o problema é de regressão supervisionada (previsão de valor numérico).

### Etapas realizadas:

1. Carregamento dos dados
2. Separação entre treino e teste
3. Treinamento do modelo
4. Avaliação com MSE (Mean Squared Error)
5. Registro do experimento com MLflow

---

## 📈 Métricas

* **MSE (Mean Squared Error)** → Avalia o erro médio quadrático das previsões.
* Quanto menor o MSE, melhor o desempenho do modelo.

---

## 🔎 Insights Obtidos

📌 Existe forte correlação positiva entre temperatura e vendas.
📌 Em dias mais quentes, a demanda aumenta significativamente.
📌 O modelo conseguiu capturar bem essa tendência linear.
📌 Pequenas variações podem ocorrer devido a ruídos simulados nos dados.

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone <seu_link_do_repositorio>
cd gelato-magico-ml
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Treinar o modelo

```bash
python src/train.py
```

### 5️⃣ Visualizar experimentos MLflow

```bash
mlflow ui
```

Abrir no navegador:

```
http://localhost:5000
```

---

## ☁ Possibilidades Futuras

🔹 Deploy em Azure Machine Learning
🔹 Criar API com FastAPI para previsão em tempo real
🔹 Adicionar novas variáveis (umidade, dia da semana, feriados)
🔹 Testar modelos mais robustos (Random Forest, XGBoost)
🔹 Implementar pipeline automatizado de MLOps

---

## 🏆 Conclusão

Este projeto demonstra a aplicação prática de:

* Machine Learning
* Regressão supervisionada
* Avaliação de métricas
* Versionamento de modelos com MLflow
* Estruturação de projeto para produção

A solução transforma dados simples (temperatura) em uma ferramenta estratégica de apoio à decisão para negócios.

---

## 👨‍💻 Autor

Desenvolvido como projeto prático para portfólio em Machine Learning e MLOps.

---

⭐ Se este projeto foi útil ou interessante, deixe uma estrela no repositório!
