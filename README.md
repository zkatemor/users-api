## Usage

All responses will have the form

```json
{
	"message": "Descriptions of what happened",
	"data": "Mixed type holding the content of the response"
}

### Список всех пользователей

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

### Информация о конкретном пользователе

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

### Удаление пользователя

**Definition**

`DELETE /user/<id>`

**Response**

- `404 Not Found` if the user does not exist
- `204 No Data`

> Также происходит удаление всех постов пользователя

### Обновление данных о пользователе

**Definition**

`PUT /user/<int:id>`

**Arguments**

В теле запроса должны быть перечислены все поля объекта в формате JSON без дополнительного заворачивания.

- `"name":string`
- `"username":string`
- `"email":string`
- `"phone":string`
- `"website":string`

**Response**

- `204 No Data` on success

### Обновление отдельных данных о пользователе

**Definition**

`PATCH /user/<int:id>`

**Arguments**

В теле запроса должны быть перечислены поля объекта, которые нужно изменить, в формате JSON без дополнительного заворачивания.

- `"name":string`
- `"username":string`
- `"email":string`
- `"phone":string`
- `"website":string`

**Response**

- `200 OK` on success

### Список всех постов

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

### Создать новый пост

**Definition**

`POST /posts`

**Arguments**

В теле запроса должны быть перечислены поля объекта в формате JSON без дополнительного заворачивания.

- `"userId":int`
- `"title":string`
- `"body":string`

**Response**

- `201 Created` on success


### Информация о конкретном посте

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
### Удаление поста

**Definition**

`DELETE /post/<int:id>`

**Response**

- `404 Not Found` if the post does not exist
- `204 No Data`

### Обновление данных о посте

**Definition**

`PUT /post/<int:id>`

**Arguments**

В теле запроса должны быть перечислены все поля объекта в формате JSON без дополнительного заворачивания.

- `"userId":int`
- `"title":string`
- `"body":string`

**Response**

- `204 No Data` on success


### Обновление отдельных данных о посте

**Definition**

`PATCH /post/<int:id>`

**Arguments**

В теле запроса должны быть перечислены поля объекта, которые нужно изменить, в формате JSON без дополнительного заворачивания.

- `"userId":int`
- `"title":string`
- `"body":string`

**Response**

- `200 OK` on success

### Список постов конкретного пользователя

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

### Удаление всех постов конкретного пользователя

**Definition**

`DELETE /user/<int:userId>/posts`

**Response**

- `404 Not Found` if the post does not exist
- `204 No Data`

### Выводит автора (пользователя) конкретного поста

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
