# Get one npc
---

Returns a json object about a single npc.

## Request

`GET host:port/npcs/:name`

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
    "name": "Tutorial Knight",
    "info": "Guides the player throughout the start of the game, ...",
    "location": "Prisoners' Quarters",
    "image": "path_to_image"
}
```

### Not found

##### HTTP Status

404

##### Body

NPC not found.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/Tutorial Knight",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
