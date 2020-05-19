# Get pickups by type
---

Returns a list of json objects with the specified pickup type.

## Request

`GET host:port/pickups/type/:type`

## URL Params

**Required**

`type=[string]`

`types: gems, minor_food, major_food, scrolls, keys`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
{
    "type": "gems",
    "pickups": [
        {
            "name": "Gold Tooth",
            "image": "path_to_image",
            "description": "A gold tooth worth (value) GOLD.",
            "value_range": "35-65",
            "sources": "One per enemy parried with the Greed Shield."
        }
    ]
}

```

### Bad Request

##### HTTP Status

400

#### Body

Invalid pickup type.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/pickups/type/gems",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
