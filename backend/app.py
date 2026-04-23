from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="myuser",
        password="mypassword"
    )
    return conn

@app.route('/api/status')
def status():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({
            "status": "success",
            "message": "Tier 2 (Flask) successfully connected to Tier 3 (PostgreSQL)! 🟢",
            "db_version": db_version[0]
        })
    except Exception as e:
        return jsonify({"status": "error", "message": f"Database connection failed: {e} 🔴"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
