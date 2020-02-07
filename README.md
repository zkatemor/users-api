# User Viewer Service

## Usage

All responses will have the form

```json
{
	"message": "Descriptions of what happened",
	"data": "Mixed type holding the content of the response"
}
```

### List all users

`GET /users`

**Response**

- `200 OK` on success

```json
[
	{
		"id": 1,
    	"name": "Leanne Graham",
    	"username": "Bret",
    	"email": "Sincere@april.biz",
    	"phone": "1-770-736-8031 x56442",
    	"website": "hildegard.org"
	},
	{
		"id": 2,
    	"name": "Ervin Howell",
    	"username": "Antonette",
    	"email": "Shanna@melissa.tv",
    	"phone": "010-692-6593 x09125",
    	"website": "anastasia.net"
	}
]
```

### Creating a new user

***Definition***

`POST /users`

**Arguments**

- `"name":string`
- `"username":string`
- `"email":string`
- `"phone":string`
- `"website":string`

**Response**

- `201 Created` on success

```json
{
	"id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org"
}
```

## Lookup user details

`GET /user/<id>`

**Response**

- `404 Not Found` if the user does not exist
- `202 OK` on success

```json
{
	"id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org"
}
```

## Delete a user

**Definition**

`DELETE /user/<id>`

**Response**

- `404 Not Found` if the user does not exist
- `204` no content

