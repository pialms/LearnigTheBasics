# What is `Requests` in Python:

The `requests` library in Python is a popular, third-party package for making HTTP requests to interact with web services, retrieve data, and communicate with APIs. It is known for its simple, "human-friendly" API that abstracts the complexities of network communication.

**To Install** the Library run the following Command: `pip install requests`

**To Use** write the following in the Scripts: `import requests`

The `Requests` library is the go-to package for making HTTP requests in Python. It abstracts the complexities of making requests behind an intuitive API. 

Though not part of Python’s standard library, it’s worth considering Requests to perform HTTP actions like GET, POST, and more.

## Key Features and Usage

The library provides an intuitive interface to perform common HTTP operations, such as: 

- `requests.get(url)`: Retrieves data from a specified URL (e.g., fetching a webpage or API data).
- `requests.post(url, data)`: Sends data to a server to create or update a resource (e.g., submitting a login form).
- `requests.put(url, data)`: Updates or replaces a target resource on the server.
- `requests.delete(url)`: Deletes a specified resource. 
- `requests.get(url, timeout=10)` : Will wait for 10s if no response is given back from the server it will automaticall get terminated.

## Response Object
After making a request, the library returns a Response object, which contains all the server's response data. 

Developers can access various attributes of this object: 

- `response.status_code`: The HTTP status code (e.g., 200 for success, 404 for not found).
- `response.text`: The content of the response in Unicode format (e.g., HTML or plain text).
- `response.json()`: A method that decodes JSON content into a Python dictionary or list if applicable.
- `response.headers`: A dictionary of the response headers.

## HTTP response status code:

HTTP response status codes are three-digit numbers issued by a server in response to a client's request, indicating whether the request was successful or if an error occurred.

They are grouped into five classes based on the first digit. The five primary classes are categorized as follows: 


- **1xx Informational**: Request received, continuing process.
- **2xx Successful**: Action successfully received and accepted.
- **3xx Redirection**: Further action needed.
- **4xx Client Error**: Bad syntax or cannot be fulfilled.
- **5xx Server Error**: Server failed to fulfill an apparently valid request. 

Common status codes include 

200 (OK), 201 (Created), 301 (Moved Permanently), 304 (Not Modified), 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 429 (Too Many Requests), 500 (Internal Server Error), and 503 (Service Unavailable).

## Important Reference Site:
1. https://requests.readthedocs.io/en/latest/
2. https://httpbin.org/