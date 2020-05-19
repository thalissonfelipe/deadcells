# Get achievements
---

Returns a list of json objects.

## Request

`GET host:port/achievements`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
    {
        "image": "path_to_image",
        "name": "Platinium",
        "description": "Unlock all trophies (PS4 only)",
        "score": "N/A",
        "trophy": "Platinium"
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
    url: "host:port/achievements",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
