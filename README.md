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


