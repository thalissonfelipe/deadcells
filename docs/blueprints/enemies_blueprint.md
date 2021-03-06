# Get enemies
---

Returns a list of json objects.

## Request

`GET host:port/enemies`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
    {
        "image": "path_to_image",
        "name": "Zombie",
        "zones": ["Prisoners' Quarters"],
        "offensive_abilities": ["Clawing attack"],
        "deffensive_abilities": "Hops backwards",
        "elite": "Yes",
        "cell_drops": "1 (33%)",
        "blueprint_drops": [
            "Blood Sword (100%)",
            "Double Crossb-o-matic (0.4%) ",
            "Boeby Outfit (1+ BSC; 0.4%)"
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
    url: "host:port/enemies",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
