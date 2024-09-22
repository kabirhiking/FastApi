An **API** (Application Programming Interface) allows different software systems to communicate with each other. It defines a set of rules for making requests and receiving responses, enabling one system to interact with another.

### Example:
If you use a weather app, the app makes a request to a weather service's API, asking for data like the current temperature. The API responds with that data, and the app displays it to you.

In Python, an API call might look like this:

```python
import requests

response = requests.get("https://api.weather.com/v1/location/city?apiKey=your_key")
print(response.json())
```

Here, the app requests weather data via the API, and the server returns it in a structured format (like JSON).



A **JSON file** (JavaScript Object Notation) is a lightweight, text-based format for storing and transmitting data. It represents data as key-value pairs, making it easy for humans to read and for machines to parse.

### Key Features:
- **Structure**: Data is organized in key-value pairs inside curly braces `{}`.
- **Data Types**: Supports simple data types like strings, numbers, booleans, arrays, and objects.
- **Use Cases**: Commonly used for configuration files, APIs, and data exchange between servers and web applications.

### Example of a JSON file:
```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Math", "Science"]
}
```

In this example:
- `name` is a string.
- `age` is a number.
- `isStudent` is a boolean.
- `courses` is an array.

JSON is widely used due to its simplicity and compatibility across different programming languages.

**virtual inveroment setup**
(https://fastapi.tiangolo.com/virtual-environments/#add-gitignore)


**```json
Command you can use to:
### Example:
If you use a weather app, the app makes a request to a weather service's API, asking for data like the current temperature. The API responds with that data, and the app displays it to you.

In Python, an API call might look like this:

```python
import requests

response = requests.get("https://api.weather.com/v1/location/city?apiKey=your_key")
print(response.json())
```

Here, the app requests weather data via the API, and the server returns it in a structured format (like JSON).

A **JSON file** (JavaScript Object Notation) is a lightweight, text-based format for storing and transmitting data. It represents data as key-value pairs, making it easy for humans to read and for machines to parse.

### Key Features:
- **Structure**: Data is organized in key-value pairs inside curly braces `{}`.
- **Data Types**: Supports simple data types like strings, numbers, booleans, arrays, and objects.
- **Use Cases**: Commonly used for configuration files, APIs, and data exchange between servers and web applications.

### Example of a JSON file:
```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Math", "Science"]
}
```

In this example:
- `name` is a string.
- `age` is a number.
- `isStudent` is a boolean.
- `courses` is an array.

JSON is widely used due to its simplicity and compatibility across different programming languages.

### Virtual Environment Setup
(https://fastapi.tiangolo.com/virtual-environments/#add-gitignore)

Command line: 
- `cd awesome-project` changes the directory to your project folder.
- `myenv\Scripts\Activate` activates the virtual environment on Windows.
- `.\.venv\Scripts\Activate` activates the virtual environment if it's located in the `.venv` folder.
- `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` sets the execution policy for the current user to allow running scripts.


**Basics kotha barta :** 

- `@app.get("/get-by-name/{student_id}")` 
- `@app.get("/get-by-name/{student_id}")` 

**Explanation**:
@app.get("/get-by-name/{student_id}"):

This is a FastAPI route decorator that defines an HTTP GET endpoint.
The "/get-by-name/{student_id}" specifies that the URL will have a path parameter called student_id. For example, a request could look like /get-by-name/1, where 1 is the student_id.
FastAPI will automatically extract the student_id from the URL and pass it to the function as an argument.
**Why Two Identical Decorators?:**

```python
Having two identical decorators (@app.get("/get-by-name/{student_id}")) does not serve any purpose and may cause unexpected behavior or an error.
FastAPI expects each route to be unique. So, you should remove one of the decorators.
```


**#short curthing**
 ```python
# //gt = getter than, lt = less than, ge = gatter than eques to , le = less than equesto
```

