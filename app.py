from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "appuser"),
            password=os.getenv("DB_PASSWORD", "apppassword"),
            database=os.getenv("DB_NAME", "appdb")
        )

        cursor = db.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()

        cursor.close()
        db.close()

        return f"""
        <h1>Praktikum Komputasi Awan</h1>
        <p>Flask + MySQL + Docker + Jenkins</p>
        <p>Status Database: Terhubung ✅</p>
        <p>Database response: {result}</p>
        """

    except Exception as e:
        return f"""
        <h1>Praktikum Komputasi Awan</h1>
        <p>Status Database: Gagal terhubung ❌</p>
        <p>Error: {e}</p>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
