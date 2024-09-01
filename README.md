# Backend

## Account App API Routes

### 1. User Registration

- **URL**: `account/api/register/`
- **Method**: `POST`
- **Description**: Register a new user.
- **Request Body**:

```json
{
  "username": "string",
  "password": "string",
  "email": "string",
  "social_media_links": {
    "facebook": "url",
    "twitter": "url"
  }
}
```

### 2. User Login

- **URL**: `api/token/`
- **Method**: `POST`
- **Description**: Login.
- **Request Body**:

```json
{
  "username": "string",
  "password": "string"
}
```

## Store App API Routes

### 1. Create Store

- **URL**: `store/`
- **Method**: `POST`
- **Description**: Create.
- **Request Body**:

```json
{
  "owner": "<user_id>",
  "name": "string",
  "logo": "file",
  "description": "string",
  "social_links": {
    "facebook": "url",
    "twitter": "url",
    "instagram": "url"
  },
  "views": 0
}
```

### 2. List Stores

- **URL**: `store/`
- **Method**: `GET`
- **Description**: Retrieves a list of all stores.
- **Response**:

```json
[
    {
        "id": "<store_id>",
        "owner": "<user_id>",
        "name": "string",
        "logo": "url",
        "description": "string",
        "social_links": {
            "facebook": "url",
            "twitter": "url",
            "instagram": "url"
        },
        "views": 0
    },
    ...
]
```

### 3. Retrieve Store Details

- **URL**: `store/`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific store.
- **Response**:

```json
{
  "id": "<store_id>",
  "owner": "<user_id>",
  "name": "string",
  "logo": "url",
  "description": "string",
  "social_links": {
    "facebook": "url",
    "twitter": "url",
    "instagram": "url"
  },
  "views": 0
}
```

### 4. Update Store

- **URL**: `store/<int:pk>`
- **Method**: `PUT`
- **Description**: Updates an existing store.
- **Request Body**:

```json
{
  "owner": "store/<int:pk>/",
  "name": "string",
  "logo": "file",
  "description": "string",
  "social_links": {
    "facebook": "url",
    "twitter": "url",
    "instagram": "url"
  },
  "views": 0
}
```

### 5. Delete Store

- **URL**: `store/<int:pk>/`
- **Method**: `DELETE`
- **Description**: Deletes a specific store.
- **Response**:

```json
{
  "message": "Store deleted successfully"
}
```

## idea App API Routes

### 1. Create Idea

- **URL**: `idea/`
- **Method**: `POST`
- **Description**: Creates a new idea.
- **Request Body**:

````json
{
    "owner": "<user_id>",
    "name": "string",
    "description": "string",
    "category": "string",   // Must be one of: 'TECH', 'FIN', 'EDU', 'HEALTH', 'AGR'
    "cost": "decimal",
    "location": "string",
    "expenses": "decimal"
}

### 2. List Ideas

- **URL**: `idea/`
- **Method**: `GET`
- **Description**: Retrieves a list of all ideas.
- **Response**:

```json
[
    {
        "id": "<idea_id>",
        "owner": "<user_id>",
        "name": "string",
        "description": "string",
        "category": "string",
        "cost": "decimal",
        "location": "string",
        "expenses": "decimal"
    },
    ...
]
````

### 3. Retrieve Idea Details

- **URL**: `idea/<int:pk>/`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific idea.
- **Response**:

```json
{
  "id": "<idea_id>",
  "owner": "<user_id>",
  "name": "string",
  "description": "string",
  "category": "string",
  "cost": "decimal",
  "location": "string",
  "expenses": "decimal"
}
```

### 4. Update Idea

- **URL**: `idea/<int:pk>/`
- **Method**: `PUT`
- **Description**: Updates an existing idea.
- **Request Body**:

```json
{
  "owner": "<user_id>",
  "name": "string",
  "description": "string",
  "category": "string", // Must be one of: 'TECH', 'FIN', 'EDU', 'HEALTH', 'AGR'
  "cost": "decimal",
  "location": "string",
  "expenses": "decimal"
}
```

### 5. Delete Idea

- **URL**: `idea/<int:pk>/`
- **Method**: `DELETE`
- **Description**: Deletes a specific idea.
- **Response**:

```json
{
  "message": "Idea deleted successfully"
}
```

## product App API Routes

### 1. Create Product

- **URL**: `product/`
- **Method**: `POST`
- **Description**: Creates a new product.
- **Request Body**:

```json
{
  "name": "string",
  "price": "decimal",
  "product_image": "file",
  "description": "string",
  "store": "<store_id>"
}
```

### 2. List Products

- **URL**: `product/`
- **Method**: `GET`
- **Description**: Retrieves a list of all products.
- **Response**:

```json
[
    {
        "id": "<product_id>",
        "name": "string",
        "price": "decimal",
        "product_image": "url",
        "description": "string",
        "store": "<store_id>"
    },
    ...
]

```

### 3. Retrieve Product Details

- **URL**: `product/<int:pk>/`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific product.
- **Response**:

```json
{
  "id": "<product_id>",
  "name": "string",
  "price": "decimal",
  "product_image": "url",
  "description": "string",
  "store": "<store_id>"
}
```

### 4. Update Product

- **URL**: `product/<int:pk>/`
- **Method**: `PUT`
- **Description**: Updates an existing product.
- **Request Body**:

```json
{
  "name": "string",
  "price": "decimal",
  "product_image": "file",
  "description": "string",
  "store": "<store_id>"
}
```

### 5. Delete Product

- **URL**: `product/<int:pk>/`
- **Method**: `DELETE`
- **Description**: Deletes a specific product.
- **Response**:

```json
{
  "message": "Product deleted successfully"
}
```

## Report App API Routes

### 1. Create Report

- **URL**: `report/`
- **Method**: `POST`
- **Description**: Creates a new report.
- **Request Body**:

```json
{
  "owner": "<user_id>",
  "description": "string",
  "funding_required": "decimal",
  "location": "string"
}
```

### 2. List Reports

- **URL**: `report/`
- **Method**: `GET`
- **Description**: Retrieves a list of all reports.
- **Response**:

```json
[
    {
        "id": "<report_id>",
        "owner": "<user_id>",
        "description": "string",
        "funding_required": "decimal",
        "location": "string"
    },
    ...
]
```

### 3. Retrieve Report Details

- **URL**: `report/<int:pk>/`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific report.
- **Response**:

```json
{
  "id": "<report_id>",
  "owner": "<user_id>",
  "description": "string",
  "funding_required": "decimal",
  "location": "string"
}
```

### 4. Update Report

- **URL**: `report/<int:pk>/`
- **Method**: `PUT`
- **Description**: Updates an existing report.
- **Request Body**:

```json
{
  "owner": "<user_id>",
  "description": "string",
  "funding_required": "decimal",
  "location": "string"
}
```

### 5. Delete Report

- **URL**: `report/<int:pk>/`
- **Method**: `DELETE`
- **Description**: Deletes a specific report.
- **Response**:

```json
{
  "message": "Report deleted successfully"
}
```
