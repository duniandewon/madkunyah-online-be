# title

My menus data looked like this before

```json
[
  {
    "name": "mac with hot chick",
    "description": "string",
    "image": "string",
    "price": 0,
    "category": "string",
    "id": 2,
    "sizes": [
      {
        "name": "party",
        "price": 125000,
        "group": "all",
        "id": 1
      },
      {
        "name": "medium",
        "price": 45000,
        "group": "all",
        "id": 2
      },
      {
        "name": "regular",
        "price": 65000,
        "group": "all",
        "id": 3
      }
    ],
    "options": []
  },
  {
    "name": "mac with hot chick",
    "description": "string",
    "image": "string",
    "price": 0,
    "category": "string",
    "id": 3,
    "sizes": [
      {
        "name": "party",
        "price": 125000,
        "group": "all",
        "id": 1
      },
      {
        "name": "medium",
        "price": 45000,
        "group": "all",
        "id": 2
      },
      {
        "name": "regular",
        "price": 65000,
        "group": "all",
        "id": 3
      }
    ],
    "options": []
  }
]
```

I wanted to add another menu-size with the update api but it replaced it entirely:

```json
// request
{
  "size_ids": [4]
}
```

```json
// Response
{
  "name": "mac with hot chick",
  "description": "string",
  "image": "string",
  "price": 0,
  "category": "string",
  "id": 2,
  "sizes": [
    {
      "name": "cup",
      "price": 20000,
      "group": "all",
      "id": 4
    }
  ],
  "
```

What if the menu update only updates general info like name, price, description and stuff, and we provide another api to add and remove options and sizes?
