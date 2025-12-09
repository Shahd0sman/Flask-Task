# 🎮 Flask Game Project

A **fun Flask web application** with a gaming-style interface, including login/signup forms and an animated character on the homepage.
<p align="center">
<img src="https://skillicons.dev/icons?i=python,sqlite,html,css,javascript,git,github,vscode&theme=dark" />
</p>

## 🌟 Features

- Login and Signup forms connected to an **SQLite database**
- **Flash messages** for login errors
- Animated **robot** moving randomly on the homepage
- Guest login and social login buttons (UI only)
- Smooth animations and interactive buttons

---

## 💻 Installation

Follow these steps to get the project running locally:

1. **Clone the repository**

```bash
git clone https://github.com/Shahd0sman/flask-game-project.git
```
2. **Go to project directory**
``` cd "flask-game-project" ```

3. **Create a virtual environment (optional but recommended)**
```python -m venv venv``

4. **Activate the virtual environment**
On Windows:
```venv\Scripts\activate```
On macOS/Linux:
source ```venv/bin/activate```

5. **Install dependencies**
```pip install -r requirements.txt```

6. **Run the Flask app**
```python home.py```

The app will run on ```http://127.0.0.1:5000/```

##🗂 Project Structure
```
flask-game-project/
│
├─ home.py            # Main Flask application
├─ players.db         # SQLite database
├─ requirements.txt   # Python dependencies
├─ templates/         # HTML templates
│   ├─ base.html
│   ├─ home.html
│   ├─ login.html
│   └─ signup.html
└─ static/            # CSS, images, GIFs
    ├─ css/
    └─ img/
```

##👩‍💻 Usage

Start the app, and visit the homepage to see the animated character.
Click PLAY to go to the login page.
Sign up for a new account or continue as a guest.
After login/signup, you can navigate to the game area (page under development).

##📌 Notes
Social login buttons (Google, Facebook) are UI only, no backend connection yet.
Make sure to use Python 3.10+ for compatibility.

##🤝 Contributing

Contributions welcome! You can:
Add new game features
Improve UI animations
Add social login backend
Enhance the game page

##📝 Author

Shahd0sman
