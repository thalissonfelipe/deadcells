# Get one boss
---

Returns a json object about a single boss.

## Request

`GET host:port/bosses/:name`

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
    "name": "The Concierge",
    "location(s)": "Black Bridge",
    "reward": ["Challenger Rune (1st kill)"],
}
```

### Not found

##### HTTP Status

404

##### Body

Boss not found.

### Internal Error

##### HTTP Status

500

##### Body

Internal Server Error.

## Sample Call

```javascript
$.ajax({
    url: "host:port/bosses/The Concierge",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
