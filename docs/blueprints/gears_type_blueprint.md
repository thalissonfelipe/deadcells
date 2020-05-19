# Get gears by type
---

Returns a list of json objects with the specified gear type.

## Request

`GET host:port/gears/type/:type`

## URL Params

**Required**

`type=[string]`

`types: malee_weapons, ranged_weapons, shields, traps_and_turrets, grenades, powers, amulets`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
{
    "type": "malee_weapons",
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
```

### Bad Request

##### HTTP Status

400

#### Body

Invalid gear type.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/gears/type/malee_weapons",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
