import pymysql  # type: ignore
from flask import Flask, request, jsonify

app = Flask(__name__)

# Konfigurasi MySQL
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Nadia16",  # Ganti dengan password MySQL Anda
    database="karyawan"
)

# Fungsi untuk menjalankan query SELECT
def select(query, values):
    with db.cursor(pymysql.cursors.DictCursor) as cursor:  # Gunakan DictCursor untuk hasil berbentuk dictionary
        cursor.execute(query, values)
        results = cursor.fetchall()
    return results

# Fungsi untuk menjalankan query INSERT
def insert(query, values):
    with db.cursor() as cursor:
        cursor.execute(query, values)
        db.commit()
    return cursor.lastrowid  # Mengembalikan ID baris terakhir yang dimasukkan

# Endpoint Flask untuk SELECT
@app.route('/karyawan', methods=['GET'])
def get_karyawan():
    try:
        query = "SELECT * FROM data_karyawann WHERE id = %s"  # Nama tabel diperbaiki
        id_karyawan = request.args.get('id')  # Ambil parameter 'id' dari query string
        results = select(query, (id_karyawan,))
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint Flask untuk INSERT
@app.route('/karyawan', methods=['POST'])
def add_karyawan():
    try:
        data = request.get_json()
        query = "INSERT INTO data_karyawann (nama, pekerjaan, usia) VALUES (%s, %s, %s)"  # Nama tabel diperbaiki
        insert(query, (data['nama'], data['pekerjaan'], data['usia']))
        return jsonify({"message": "Data berhasil ditambahkan!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
