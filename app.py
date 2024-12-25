from flask import Flask, Response, request
from dicttoxml import dicttoxml
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Depo Durumu (Başlangıç verisi)
warehouse_status = {
    "statusDate": "2024-12-22",
    "location": {
        "id": "1",
        "name": "Main Warehouse",
        "items": [
            {"sku": "12345", "name": "Smartphone", "quantity": 150, "status": "In Stock"},
            {"sku": "67890", "name": "Wireless Earbuds", "quantity": 50, "status": "Low Stock"}
        ]
    }
}

# Root Endpoint (Karşılama Mesajı)
@app.route('/', methods=['GET'])
def home():
    return "Merhaba! Depo durumu için /warehouse/status GET ve POST metodlarını kullanabilirsiniz."

# GET Endpoint: Depo Durumunu Döndür
@app.route('/warehouse/status', methods=['GET'])
def get_warehouse_status():
    xml_data = dicttoxml(warehouse_status, custom_root='warehouse', attr_type=False)
    # XML verisini konsola yazdır
    print("Alınan XML Verisi:\n", xml_data.decode('utf-8'))
    return Response(xml_data, mimetype='application/xml')

# POST Endpoint: Depo Durumunu Güncelle
@app.route('/warehouse/status', methods=['POST'])
def update_warehouse_status():
    try:
        # İstekten gelen XML verisini al
        xml_data = request.data.decode('utf-8')

        # XML verisini parse et
        root = ET.fromstring(xml_data)

        # Yeni depo durumunu al
        global warehouse_status
        warehouse_status["statusDate"] = root.find("statusDate").text
        location = root.find("location")
        warehouse_status["location"]["id"] = location.get("id")
        warehouse_status["location"]["name"] = location.find("name").text
        warehouse_status["location"]["items"] = []

        for item in location.find("items").findall("item"):
            warehouse_status["location"]["items"].append({
                "sku": item.find("sku").text,
                "name": item.find("name").text,
                "quantity": int(item.find("quantity").text),
                "status": item.find("status").text
            })

        return "Depo durumu güncellendi!", 200
    except Exception as e:
        return f"Hata: {e}", 400


if __name__ == '__main__':
    app.run(debug=True)
