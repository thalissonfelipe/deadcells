# Get one rune
---

Returns a json object about a single rune.

## Request

`GET host:port/runes/:name`

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
    "name": "Vine Rune",
    "image": "path_to_image",
    "biome": "Promenade of the Condemned",
    "location": "In a room accessed by entering a door found at the base of a large overhang",
    "enemy": "Undead Archer",
    "ability": "Ability to sprout vines from special green blobs.",
    "access": [
        "Toxic Sewers",
        "Ramparts",
        "Dilapidated Arboretum (when paired with Teleportation Rune)"
    ]
}
```

### Not found

##### HTTP Status

404

##### Body

Rune not found.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/runes/Vine Rune",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
