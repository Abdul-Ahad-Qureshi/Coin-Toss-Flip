
##🪙 Coin Toss Game
A fun **Flask-based web application** where users can sign up, log in, and test their luck with a **coin toss game** 🎮.
Every toss is stored in the database so you can track your history and stats.

---

## ✨ Features

✔️ User authentication (Signup, Login, Logout)
✔️ Secure password hashing with Flask-Login
✔️ Fair coin toss with random outcomes (Heads/Tails)
✔️ Game history stored in SQLite database
✔️ Simple and clean Bootstrap-powered interface

---

## ⚙️ Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/yourusername/coin-toss-game.git
cd coin-toss-game

# Create and activate venv
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will be available at:
👉 `http://127.0.0.1:5000/`

---

## 📂 Project Structure

```
Coin Toss Game/
│── app.py              # Main Flask app
│── database.py         # Database initialization
│── models.py           # User & GameResult models
│── requirements.txt    # Dependencies
│── templates/          # HTML templates (index, login, signup, profile, etc.)
│── static/             # CSS, JS, images
```

---

## 🚀 Future Enhancements

* 🏆 Leaderboard for top players
* 📊 Player statistics (win/loss ratio)
* 🎨 Coin toss animation
* 🌍 Deployment on Heroku/Render

---




