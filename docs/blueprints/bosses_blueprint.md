# Get bosses
---

Returns a list of json objects.

## Request

`GET host:port/bosses`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
    {
        "name": "The Concierge",
        "location(s)": "Black Bridge",
        "reward": ["Challenger Rune (1st kill)"],
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
    url: "host:port/bosses",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
