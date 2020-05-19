# Get outfits
---

Returns a list of json objects.

## Request

`GET host:port/outfits`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
    {
        'image': 'path_to_image',
        'name': 'Classic Outfit',
        'description': 'You went through a lot with this one, ...',
        'location': 'N/A',
        'difficulty_required': 'N/A',
        'cell_cost': 'N/A',
        'reference': ''
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
    url: 'host:port/outfits',
    dataType: 'json',
    type : 'GET',
    success : function(data) {
        console.log(data);
    }
});
```
