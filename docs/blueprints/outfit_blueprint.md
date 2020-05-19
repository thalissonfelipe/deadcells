# Get one outfit
---

Returns a json object about a single outfit.

## Request

`GET host:port/outfits/:name`

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
    "name": "Classic Outfit",
    "description": "You went through a lot with this one, ...",
    "location": "N/A",
    "difficulty_required": "N/A",
    "cell_cost": "N/A",
    "reference": ""
}
```

### Not found

##### HTTP Status

404

##### Body

Outfit not found.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/outfits/Classic Outfit",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
