# 🛡️ SecPro — Secure & Proactive Cybersecurity Toolkit



[![Coverage](https://codecov.io/gh/eurocybersecurite/SecPro/branch/main/graph/badge.svg)](https://codecov.io/gh/eurocybersecurite/SecPro)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=eurocybersecurite_SecPro&metric=security_rating)](https://sonarcloud.io/dashboard?id=eurocybersecurite_SecPro)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=eurocybersecurite_SecPro&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=eurocybersecurite_SecPro)
[![License](https://img.shields.io/github/license/eurocybersecurite/SecPro)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)

---

## 📖 Description

**SecPro** est une application web & API conçue pour **auditer**, **détecter** et **corriger** les vulnérabilités de vos systèmes et applications.  
Elle combine des fonctionnalités d’**audit de cybersécurité**, de **planification de scans**, et de **remédiation automatisée**.

🔑 Points forts :
- Interface web intuitive (Flask + Bootstrap)
- API REST sécurisée (JWT, Swagger/OpenAPI)
- Gestion des rôles & utilisateurs (RBAC + 2FA)
- Génération de rapports 📊 (PDF/CSV)
- 30+ fonctionnalités cybersécurité (audits, remédiations, gouvernance)

---

## 🚀 Fonctionnalités principales

✅ Scan des dépendances (pip-audit / safety)  
✅ Audit de configurations (SSH, TLS, headers HTTP)  
✅ Détection OWASP Top10 (XSS, SQLi…)  
✅ Gestion des actifs & cartographie réseau  
✅ Génération de scripts de remédiation  
✅ Notifications (Email, Slack, Webhooks)  
✅ Rapports détaillés (PDF/CSV)  
✅ API REST documentée (Swagger/OpenAPI)  
✅ Dashboard intuitif avec KPI sécurité  

📌 👉 La liste complète des **30 fonctionnalités** se trouve dans [docs/FUNCTIONALITIES.md](docs/FUNCTIONALITIES.md).

---

## 🏗️ Architecture du projet
```bash
SecPro/
├─ app.py # Entrée principale Flask
├─ requirements.txt # Dépendances Python
├─ Dockerfile # Build container
├─ docker-compose.yml # Orchestration multi-services
├─ .github/workflows/ # CI/CD GitHub Actions
│ ├─ ci.yml
│ └─ tests.yml
├─ secpro/ # Code source principal
│ ├─ init.py
│ ├─ config.py
│ ├─ models.py
│ ├─ core/ # Modules cybersécurité (audits, remédiations…)
│ ├─ routes/ # Endpoints Web et API
│ ├─ services/ # Services externes (SIEM, alertes…)
│ ├─ templates/ # Vues HTML (Jinja2)
│ └─ static/ # Fichiers statiques (CSS/JS/images)
├─ tests/ # Tests unitaires et intégration
├─ docs/ # Documentation
│ ├─ FUNCTIONALITIES.md # Liste des fonctionnalités
│ └─ assets/ # Images & logos
└─ migrations/ # Gestion de la base (Flask-Migrate)

---
```
## 📸 Captures d’écran

- **Dashboard**  
 

- **Rapport de scan**  

---

## ⚙️ Installation & lancement

### 🔧 Prérequis
- Python **3.11+**
- Pip & virtualenv
- Docker (optionnel mais recommandé)

### 🖥️ Installation locale
```bash
git clone https://github.com/eurocybersecurite/SecPro.git
cd SecPro

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt

flask db upgrade
flask run
👉 Application dispo sur : http://localhost:5000
```

### 🐳 Lancement via Docker
```bash
docker-compose up --build
```

### 🧪 Tests & Qualité
```bash
# Lancer les tests unitaires :
pytest -q
# Analyse de sécurité statique & dépendances :
flake8 .
bandit -r secpro -lll
pip-audit
```

### 🔐 Bonnes pratiques sécurité
- Secrets stockés via variables d’environnement (.env)
- CSRF protection activée
- JWT pour l’API + sessions sécurisées
- TOTP 2FA activable pour les comptes
- Logs structurés avec audit trail
- HTTPS obligatoire en production

### 📤 Déploiement GitHub
```bash
git init
git add .
git commit -m "feat: initial SecPro release"
git branch -M main
git remote add origin https://github.com/eurocybersecurite/SecPro.git
git push -u origin main
```

---

## 👥 Auteurs & contributeurs

- Équipe Eurocybersecurite  
- Contributions bienvenues via Pull Requests

## 📜 Licence

Distribué sous licence. Voir [LICENSE](LICENSE).
