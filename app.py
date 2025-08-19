# app.py
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import User, GameResult, db
from database import init_db
import random
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coin_toss.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
init_db(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('signup'))
        
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists!', 'danger')
            return redirect(url_for('signup'))
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('profile'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    # Get user's game history
    game_history = GameResult.query.filter_by(user_id=current_user.id).order_by(GameResult.timestamp.desc()).limit(10).all()
    
    # Calculate stats
    total_games = GameResult.query.filter_by(user_id=current_user.id).count()
    wins = GameResult.query.filter_by(user_id=current_user.id, result='Win').count()
    losses = total_games - wins
    win_percentage = round((wins / total_games) * 100, 2) if total_games > 0 else 0
    
    return render_template('profile.html', 
                        user=current_user,
                        game_history=game_history,
                        total_games=total_games,
                        wins=wins,
                        losses=losses,
                        win_percentage=win_percentage)

@app.route('/game', methods=['GET', 'POST'])
@login_required
def game():
    result = None
    user_choice = None
    coin_result = None
    
    if request.method == 'POST':
        user_choice = request.form.get('choice')
        coin_result = random.choice(['heads', 'tails'])
        
        if user_choice == coin_result:
            result = 'Win'
            flash('Congratulations! You won!', 'success')
        else:
            result = 'Loss'
            flash('Sorry, better luck next time!', 'warning')
        
        # Save game result
        new_result = GameResult(
            user_id=current_user.id,
            user_choice=user_choice,
            coin_result=coin_result,
            result=result,
            timestamp=datetime.utcnow()
        )
        db.session.add(new_result)
        db.session.commit()
    
    return render_template('game.html', 
                        result=result, 
                        user_choice=user_choice, 
                        coin_result=coin_result)

if __name__ == '__main__':
    app.run(debug=True)