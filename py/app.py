from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    barcode = request.form.get('barcode')  # รับค่าจากฟอร์ม
    if barcode == "1234567890":  # ตัวอย่างข้อมูล
        result = {"status": "Passed", "message": f"Barcode {barcode} is valid."}
    else:
        result = {"status": "Failed", "message": f"Barcode {barcode} is invalid."}

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
