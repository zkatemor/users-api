## Usage

All responses will have the form

```json
{
	"message": "Descriptions of what happened",
	"data": "Mixed type holding the content of the response"
}
```
### Users list

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

### User's details

`GET /user/<int:id>`

**Response**

- `404 Not Found` if the user does not exist
- `200 OK` on success

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

### Delete user

**Definition**

`DELETE /user/<id>`

**Response**

- `404 Not Found` if the user does not exist
- `204 No Data`

> + delete all user's posts

### Update user

**Definition**

`PUT /user/<int:id>`

**Arguments**

JSON

- `"name":string`
- `"username":string`
- `"email":string`
- `"phone":string`
- `"website":string`

**Response**

- `204 No Data` on success

### Update some user's detail

**Definition**

`PATCH /user/<int:id>`

**Arguments**

JSON

- `"name":string`
- `"username":string`
- `"email":string`
- `"phone":string`
- `"website":string`

**Response**

- `200 OK` on success

### Posts list

`GET /posts`

**Response**

- `200 OK` on success

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  }
]
```

### Create new post

**Definition**

`POST /posts`

**Arguments**

JSON

- `"userId":int`
- `"title":string`
- `"body":string`

**Response**

- `201 Created` on success


### Post's details

`GET /post/<int:id>`

**Response**

- `404 Not Found` if the post does not exist
- `200 OK` on success

```json
{
	"userId": 1,
    	"id": 1,
    	"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    	"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```
### Delete post

**Definition**

`DELETE /post/<int:id>`

**Response**

- `404 Not Found` if the post does not exist
- `204 No Data`

### Update post's detail

**Definition**

`PUT /post/<int:id>`

**Arguments**

JSON

- `"userId":int`
- `"title":string`
- `"body":string`

**Response**

- `204 No Data` on success


### Update some post's detail

**Definition**

`PATCH /post/<int:id>`

**Arguments**

JSON

- `"userId":int`
- `"title":string`
- `"body":string`

**Response**

- `200 OK` on success

### User's posts list

**Definition**

`GET /user/<int:userId>/posts`

**Response**

- `200 OK` on success

```json
 {
	"id": 11,
	"userId": 2,
	"title": "et ea vero quia laudantium autem",
	"body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\naccusamus in eum beatae sit\nvel qui neque voluptates ut commodi qui incidunt\nut animi commodi"
 },
 {
	"id": 12,
	"userId": 2,
	"title": "in quibusdam tempore odit est dolorem",
	"body": "itaque id aut magnam\npraesentium quia et ea odit et ea voluptas et\nsapiente quia nihil amet occaecati quia id voluptatem\nincidunt ea est distinctio odio"
 }
```

### Delete user's post

**Definition**

`DELETE /user/<int:userId>/posts`

**Response**

- `404 Not Found` if the post does not exist
- `204 No Data`

### Post's author

`GET /post/<int:id>/user`

**Response**

- `404 Not Found` if the user does not exist
- `200 OK` on success

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
