# Zapier-Barcode-Reader

Zapier integration for [Dynamsoft Barcode Reader](https://www.dynamsoft.com/barcode-reader/overview).

We can scan barcodes and trigger zaps.

[Online demo](https://zapier-barcode-reader.vercel.app/scanner.html)

## API

You can deploy the server on your own and create an integration using the API.

* `/code`
   
   Methods: `GET`, `POST`

   Create a new barcode using the `POST` method and query scanned new barcodes by UUID using the `GET` method.

   Arguments:

   * `keep` (optional): pass this argument to avoid clearing the barcodes
   * `barcode` (optional): string of scanned barcode
   * `uuid`: unique ID of a device. Barcodes will stored according to the UUID.

   Sample Response:

   ```json
   [
       {
           "id":1,
           "barcode":"9780321344755"
       }
   ]
   ```

* `/auth`

   Methods: `GET`

   This always returns `{"success":true}`.


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
