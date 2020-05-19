# Get one gear
---

Returns a json object about a single gear.

## Request

`GET host:port/gears/name/:name`

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
    "image": "path_to_image",
    "name": "Rusty Sword",
    "description": "Kills things. Sometimes...",
    "location": "Starter melee weapon until Random Starter Melee Weapon is purchased (found in secret tile near the place where you start afterwards)",
    "base_dps": "119 DPS",
    "special_dps": "N/A",
    "scaling": "path_to_image",
    "type": "malee_weapons"
}
```

### Not found

##### HTTP Status

404

##### Body

Gear not found.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/gears/name/Rusty Sword",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
