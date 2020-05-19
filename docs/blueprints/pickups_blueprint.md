# Get pickups
---

Returns a list of json objects.

## Request

`GET host:port/pickups`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
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
]
```

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/pickups",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
