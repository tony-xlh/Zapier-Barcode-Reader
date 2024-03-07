# Zapier-Barcode-Reader

Zapier integration for Dynamsoft Barcode Reader.

We can scan barcodes and trigger zaps.


## Sample Usage

We can scan an ISBN barcode of a book, get its info and send it to notion.


![image](https://github.com/tony-xlh/Zapier-Barcode-Reader/assets/112376616/dca9e921-c1b0-4101-b08e-5a7786a1bda1)


JavaScript used:

```js
output = [];
let response = await fetch("https://www.googleapis.com/books/v1/volumes?q=isbn:"+inputData.barcode);
let object = await response.json()
let items = object["items"]
if (items.length>0) {
  let item = items[0];
  let title = item["volumeInfo"]["title"];
  let desc = item["volumeInfo"]["description"]; 
  let authors = item["volumeInfo"]["authors"].join(" ");
  output = [{"title":title,"desc":desc,"authors":authors}];
}
```
