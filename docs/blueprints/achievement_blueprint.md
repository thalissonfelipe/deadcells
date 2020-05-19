# Get one achievement
---

Returns a json object about a single achievement.

## Request

`GET host:port/achievements/:name`

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
    "name": "Platinium",
    "description": "Unlock all trophies (PS4 only)",
    "score": "N/A",
    "trophy": "Platinium"
}
```

### Not found

##### HTTP Status

404

##### Body

Achievement not found.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/achievements/Platinium",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
