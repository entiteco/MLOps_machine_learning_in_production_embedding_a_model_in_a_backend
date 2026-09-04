
# House Price Prediction - MLOps API & UI

Déploiement de bout en bout d'un modèle de Machine Learning pour l'estimation de prix immobiliers, intégrant une interface Streamlit, une API REST FastAPI et la conteneurisation avec Docker.

---

## Structure du projet

```text
├── houses.csv             # Dataset d'entraînement
├── train_model.py         # Script d'entraînement du modèle
├── regression.joblib      # Modèle sérialisé
├── model_app.py           # Interface utilisateur Streamlit
├── api.py                 # API REST FastAPI
├── test_api.py            # Tests de l'API
├── requirements.txt       # Dépendances Python
└── Dockerfile             # Fichier de conteneurisation Docker
```
