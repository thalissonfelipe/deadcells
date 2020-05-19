# Get mutations by type
---

Returns a list of json objects with the specified mutation type.

## Request

`GET host:port/mutations/type/:type`

## URL Params

**Required**

`type=[string]`

`types: brutality, tactics, survival, colorless`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
{
    "type": "brutality",
    "mutations": [
        {
            "name": "Killer Instinct",
            "image": "path_to_image",
            "description": "Reduces the cooldown of your skills by [0.4 base] seconds for each enemy killed in hand to hand combat.",
            "acquisition_method": "N/A (Always available)",
            "unlock_cost": "N/A",
            "notes": [
                "Reduces your skill cooldowns when you kill an enemy with a Melee weapon. Starts at 0.4 seconds and has a cap of 3 seconds at 25+ Brutality."
            ]
        }
    ]
}
```

### Bad Request

##### HTTP Status

400

#### Body

Invalid mutation type.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/mutations/type/brutality",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
