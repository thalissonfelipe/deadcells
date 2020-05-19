# Get gears
---

Returns a list of json objects.

## Request

`GET host:port/gears`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
    {
        "type": "malee",
        "gears": [
            {
                "image": "path_to_image",
                "name": "Rusty Sword",
                "description": "Kills things. Sometimes...",
                "location": "Starter melee weapon until Random Starter Melee Weapon is purchased (found in secret tile near the place where you start afterwards)",
                "base_dps": "119 DPS",
                "special_dps": "N/A",
                "scaling": "path_to_image"
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
    url: "host:port/gears",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
