# 🖱️ DZ AutoClicker Premium

Un script d'Auto-Clicker élégant et minimaliste développé en Python avec **CustomTkinter**.
Idéal pour simuler une activité de présence continue (ex: éviter le statut "Absent" sur Microsoft Teams ou Discord).

---

## 🚀 Fonctionnalités

* **Interface Premium** : Un magnifique Dark Mode épuré.
* **Simple d'utilisation** : Pas de configuration complexe, juste un gros bouton Démarrer/Arrêter.
* **Intervalle Personnalisable** : Paramétrez le temps entre chaque clic en un clin d'œil (par défaut : 30 secondes).
* **Mode Arrière-Plan** : Le processus de clics fonctionne de manière asynchrone sans bloquer l'interface de l'application.

## 📥 Installation

Si vous souhaitez utiliser le code source directement, voici comment l'installer :

1. Clonez ce dépôt.
   ```cmd
   git clone https://github.com/yacinus17/DZ-Auto-Clicker.git
   cd DZ-Auto-Clicker
   ```
2. Créez un environnement virtuel (optionnel mais recommandé).
   ```cmd
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Installez les dépendances requises.
   ```cmd
   pip install -r requirements.txt
   ```

## 🎮 Utilisation

Exécutez simplement le programme source :
```cmd
python main.py
```

> ⚠️ Placez simplement la fenêtre de l'application dans un coin, cliquez sur "Démarrer", et positionnez votre curseur à l'endroit où vous voulez que les clics s'exécutent.

## 🛠️ Compilation en Exécutable (.exe)

Vous pouvez compiler ce projet en un unique fichier `.exe` pour pouvoir le distribuer sans avoir besoin d'installer Python.

Assurez-vous d'avoir installé `pyinstaller` (inclus dans l'environnement si vous le souhaitez) :
```cmd
pip install pyinstaller
```

Compilez le projet avec la commande suivante :
```cmd
pyinstaller --noconsole --onefile --windowed --name "AutoClicker Premium" main.py
```
Le fichier `.exe` résultant se trouvera dans le dossier `dist/`.

## ⚙️ Dépendances

- `customtkinter` : Pour l'interface graphique moderne.
- `pynput` : Pour le contrôle précis de la souris.

## 📝 Licence

Ce projet est libre de droits. Utilisez-le comme bon vous semble !
