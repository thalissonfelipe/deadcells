# Get npcs
---

Returns a list of json objects.

## Request

`GET host:port/npcs`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
    {
        'name': 'Tutorial Knight',
        'info': 'Guides the player throughout the start of the game, ...',
        'location': 'Prisoners\' Quarters',
        'image': 'path_to_image'
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
    url: 'host:port/npcs',
    dataType: 'json',
    type : 'GET',
    success : function(data) {
        console.log(data);
    }
});
```
