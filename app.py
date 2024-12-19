from flask import Flask, jsonify, request, make_response  # type: ignore
from model import Data

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def hello():
    data = [{
        'nama': 'Galih',
        'pekerjaan': 'Web Engineer',
        'umur': '27'
    }]
    return make_response(jsonify({'data': data}), 200)

@app.route('/karyawan', methods=['GET', 'POST', 'PUT', 'DELETE'])
def karyawan():
    try:
        # Panggil class model database
        dt = Data()
        values = ()
        
        # Jika Method GET
        if request.method == 'GET':
            id_ = request.args.get("id")
            if id_:
                query = "SELECT * FROM data_karyawann WHERE id = %s"
                values = (id_,)
            else:
                query = "SELECT * FROM data_karyawann"
            data = dt.get_data(query, values)
        
        # Jika Method POST
        elif request.method == 'POST':
            datainput = request.json
            nama = datainput['nama']
            pekerjaan = datainput['pekerjaan']
            usia = datainput['usia']
            
            query = "INSERT INTO data_karyawann (nama, pekerjaan, usia) VALUES (%s, %s, %s)"
            values = (nama, pekerjaan, usia)
            dt.insert_data(query, values)
            data = [{
                'pesan': 'berhasil menambah data'
            }]
        
        # Jika Method PUT
        elif request.method == 'PUT':
            datainput = request.json
            id_ = datainput['id']
            values = []
            query = "UPDATE data_karyawann SET"
            
            if 'nama' in datainput:
                query += " nama = %s,"
                values.append(datainput['nama'])
            if 'pekerjaan' in datainput:
                query += " pekerjaan = %s,"
                values.append(datainput['pekerjaan'])
            if 'usia' in datainput:
                query += " usia = %s,"
                values.append(datainput['usia'])
            
            # Hapus koma terakhir dan tambahkan WHERE clause
            query = query.rstrip(',') + " WHERE id = %s"
            values.append(id_)
            
            dt.insert_data(query, tuple(values))
            data = [{
                'pesan': 'berhasil mengubah data'
            }]
        
        # Jika Method DELETE
        elif request.method == 'DELETE':
            id_ = request.args.get("id")
            query = "DELETE FROM data_karyawann WHERE id = %s"
            values = (id_,)
            dt.insert_data(query, values)
            data = [{
                'pesan': 'berhasil menghapus data'
            }]
        
        else:
            return make_response(jsonify({'error': 'Method tidak diizinkan'}), 405)

    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    
    return make_response(jsonify({'data': data}), 200)

if __name__ == "__main__":
    app.run(debug=True, port=5003)