# Get one mutation
---

Returns a json object about a single mutation.

## Request

`GET host:port/mutations/name/:name`

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
    'name': 'Killer Instinct',
    'image': 'path_to_image',
    'description': 'Reduces the cooldown of your skills by [0.4 base] seconds for each enemy killed in hand to hand combat.',
    'acquisition_method': 'N/A (Always available)',
    'unlock_cost': 'N/A',
    'notes': [
        'Reduces your skill cooldowns when you kill an enemy with a Melee weapon. Starts at 0.4 seconds and has a cap of 3 seconds at 25+ Brutality.'
    ]
}
```

### Not found

##### HTTP Status

404

##### Body

Mutation not found.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: 'host:port/mutations/name/Killer Instinct',
    dataType: 'json',
    type : 'GET',
    success : function(data) {
        console.log(data);
    }
});
```
