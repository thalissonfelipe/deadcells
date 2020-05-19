# Get biomes
---

Returns a list of json objects.

## Request

`GET host:port/biomes`

## Request Response

### Success

##### HTTP Status

200

##### Body

```json
[
    {
        "name": "Prisoners Quarters",
        "location": "Above the Promenade of the Condemned",
        "next_biome(s)": "Promenade of the Condemned, Toxic Sewers, Dilapidated Arboretum",
        "enemy_tier": "1 (0 BSC) / 6 (5 BSC)",
        "gear_level": "1 (0 BSC) / 4 (5 BSC)",
        "scrolls": "2 Scrolls of Power",
        "blueprints_from_secret_areas": "Quick Bow, Broadsword, Disengagement, Golden Outfit, Crowbar, HEV Outfit",
        "enemies": [
            "Zombies, Shield Bearers, Grenadiers, Undead Archers",
            "Rancid Rat, Knife Throwers (1+ BSC, replaces Undead Archers)",
            "Guardians (2+ BSC)",
            "Rampagers (3+ BSC)",
            "Failed Experiments, (replaces Zombies) Inquisitors (4+ BSC)"
        ],
        "hazards": "Spikes, rotating spiked balls",
        "wandering_elite_chance": "0%",
        "elite_room_chance": "5%",
        "stage": "1"
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
    url: "host:port/biomes",
    dataType: "json",
    type : "GET",
    success : function(data) {
        console.log(data);
    }
});
```
