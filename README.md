# 🚀 My First Real Project

> A full-stack web application built with Python and Flask on the backend, featuring an SQLite database and a responsive user interface.

---

## 📌 About The Project

**My First Real Project** is a web application focused on robust backend logic, structured data management, and a smooth user experience.

### Key Features:
* **User Authentication:** Secure registration, login, and session management.
* **Backend Logic:** Full implementation of CRUD operations and server-side data processing.
* **Database Management:** Structured storage and relational queries using SQLite.
* **Responsive UI:** Clean and functional frontend interface for seamless interaction.

---

## 🛠️ Built With

* **Backend:** Python 3, Flask
* **Database:** SQLite
* **Frontend:** HTML5, CSS3, JavaScript
* **Version Control:** Git, GitHub

---

## ⚙️ Getting Started

Follow these steps to get a local copy up and running on your machine.

### 1. Clone the repository
<pre>
git clone [https://github.com/filiplukic95/MyFirstRealProject.git](https://github.com/filiplukic95/MyFirstRealProject.git)
cd MyFirstRealProject
</pre>

### 2. Create and activate a virtual environment

**Windows:**
<pre>
python -m venv venv
venv\Scripts\activate
</pre>

**Linux / macOS:**
<pre>
python3 -m venv venv
source venv/bin/activate
</pre>

### 3. Install dependencies
<pre>
pip install -r requirements.txt
</pre>

### 4. Environment Setup
Create a `.env` file in the root directory and add your environment variables:
<pre>
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
</pre>

### 5. Run the application
<pre>
flask run
</pre>

Open your browser and navigate to `[http://127.0.0.1:5000/](http://127.0.0.1:5000/)`

---

## 📂 Project Structure

<pre>
MyFirstRealProject/
├── static/              # CSS, JavaScript, and static assets
├── templates/           # HTML templates
├── app.py               # Main application logic and routes
├── database.db          # SQLite database
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
</pre>

---

## 🎯 Roadmap

- [x] Implement core backend logic and database models
- [x] Set up user authentication and session routing
- [ ] Integrate online payment gateway
- [ ] Add unit tests for backend logic

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
