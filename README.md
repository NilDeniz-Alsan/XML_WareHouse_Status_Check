# XML WareHouse  Status Check

This application offers two basic HTTP endpoints to manage and display the inventory status of a warehouse:
GET Method: Returns the current status of the warehouse in XML format.
POST Method: Updates the status of the warehouse with the sent XML data.

Description of code blocs:

1. Initial Data (warehouse_status): A warehouse_status dictionary is
defined at the beginning of the code. This dictionary contains the
current status of the warehouse:
statusDate: The date the warehouse status was last updated.
location: Contains warehouse information, ID, name and products
(items) in it.
items: Information such as SKU (stock code), name, quantity and
stock status of the products.
Root Endpoint (/): When the application sends a GET request to the
root URL (root), it returns a welcome message:
“Merhaba! Depo durumu için /warehouse/status GET ve POST metodlarını kullanabilirsiniz.”

2. GET Endpoint: /warehouse/status: When the user makes a GET request to this endpoint, warehouse_status data is returned in XML
format:
<?xml version="1.0" encoding="UTF-8"
?><warehouse><statusDate>2024-12-23</statusDate><location><id>2
</id><name>Secondary
Warehouse</name><items><item><sku>54321</sku><name>Laptop</
name><quantity>25</quantity><status>In
Stock</status></item><item><sku>98765</sku><name>Keyboard</na
me><quantity>100</quantity><status>In
Stock</status></item></items></location></warehouse>

dicttoxml library converts Python dictionary to XML.XML data is returned in application/xml format.

3. POST Endpoint: /warehouse/status:The user can send the warehouse status in XML format by making a POST request to this
endpoint. The sent XML updates the warehouse_status variable.The data
received with request.data is received and parsed as XML (ET.fromstring). statusDate, location, and items information are read
from the new XML and updated. After the update, the server returns a successful response: "Warehouse status updated!".

4. Error Management: If an error occurs during the update, the
application returns an error response with the message "Error: {e}".
## Output
