# Get one pickup
---

Returns a json object about a single pickup.

## Request

`GET host:port/pickups/name/:name`

## URL Params

**Required**

`name=[string]`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
{
    "name": "Gold Tooth",
    "image": "path_to_image",
    "description": "A gold tooth worth (value) GOLD.",
    "value_range": "35-65",
    "sources": "One per enemy parried with the Greed Shield.",
    "type": "gems"
}
```

### Not found

##### HTTP Status

404

##### Body

Pickup not found.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/pickups/name/Gold Tooth",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
