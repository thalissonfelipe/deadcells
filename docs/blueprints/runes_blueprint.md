# Get runes
---

Returns a list of json objects.

## Request

`GET host:port/runes`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
    {
        'name': 'Vine Rune',
        'image': 'path_to_image',
        'biome': 'Promenade of the Condemned',
        'location': 'In a room accessed by entering a door found at the base of a large overhang',
        'enemy': 'Undead Archer',
        'ability': 'Ability to sprout vines from special green blobs.',
        'access': [
            'Toxic Sewers',
            'Ramparts',
            'Dilapidated Arboretum (when paired with Teleportation Rune)'
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
    url: 'host:port/runes',
    dataType: 'json',
    type : 'GET',
    success : function(data) {
        console.log(data);
    }
});
```
