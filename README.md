# Django Polls Application

A simple polling application built using Django. Users can view available questions, select an option, cast votes, and view the results.

## Features

- View the latest poll questions.
- Open individual poll questions.
- Vote for a choice.
- View updated voting results.
- Handle submissions without a selected choice.
- Manage questions and choices through Django Admin.
- Automated tests for core functionality.

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/codeman2008/poll.git
   cd poll
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install Django:

   ```bash
   pip install django
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/polls/` in your browser.

## Running Tests

Run the automated tests using:

```bash
python manage.py test polls
```

## Web Development Concepts

### 1. What happens when you enter a URL in the browser and press Enter?

1. The browser interprets the URL and identifies the protocol, domain name, and requested path.
2. DNS (Domain Name System) translates the domain name into an IP address.
3. The browser establishes a connection with the server using TCP and, for HTTPS, performs a TLS handshake.
4. The browser sends an HTTP request to the server.
5. The server processes the request and generates an HTTP response.
6. The browser receives the response and renders the content. It may request additional resources such as CSS, JavaScript, and images.

### 2. What are a client and a server? How do they communicate?

A client is a device or application that requests a service or resource. A web browser is an example of a client.

A server is a computer or software application that receives requests, processes them, and sends responses.

They communicate using a request-response model. In web applications, this communication generally happens through HTTP or HTTPS over a network.

### 3. What is HTTP? What are HTTP requests and responses?

HTTP stands for Hypertext Transfer Protocol. It is an application-layer protocol used for communication between clients and web servers.

An HTTP request is sent by the client to ask the server for a resource or to perform an operation.

An HTTP request generally contains:
- Request method, such as GET or POST.
- URL or path.
- HTTP headers containing additional information.
- An optional body containing data.

An HTTP response is sent by the server after processing the request.

An HTTP response generally contains:
- Status code indicating the result.
- Response headers containing metadata.
- Response body containing the requested content or other data.

### 4. What is the difference between GET and POST?

**GET:**
- Used to retrieve data from a server.
- Parameters are commonly included in the URL.
- Usually does not modify server-side data.
- Can be bookmarked and cached in appropriate circumstances.

**POST:**
- Used to submit data to a server.
- Data is generally included in the request body.
- Commonly used for operations that create or modify data.
- Is not normally cached like GET requests.

In this polling application, GET is used to display questions, while POST is used to submit a vote.

### 5. Explain HTTP status codes 200, 302, 404, and 500.

- **200 OK:** The request was successful, and the server returned the requested resource.
- **302 Found:** The requested resource is temporarily available at another URL. The browser is redirected.
- **404 Not Found:** The requested resource could not be found on the server.
- **500 Internal Server Error:** The server encountered an unexpected condition that prevented it from fulfilling the request.

### 6. What are HTML, CSS, and JavaScript? What are their roles?

**HTML (HyperText Markup Language):** Defines the structure and content of a webpage, such as headings, paragraphs, links, forms, and buttons.

**CSS (Cascading Style Sheets):** Controls the appearance and layout of webpages, including colours, fonts, spacing, and responsiveness.

**JavaScript:** Adds interactivity and dynamic behaviour to webpages, such as responding to user actions and updating content without reloading the page.

Together, they form the foundation of frontend web development.

### 7. How do websites remember users? Explain cookies and sessions.

HTTP is stateless, meaning each request is independent by default. The server does not automatically remember previous requests from the same user.

Websites use cookies and sessions to maintain information across requests.

**Cookies:**
- Small pieces of data stored in the user's browser.
- Sent to the server with subsequent requests when applicable.
- Can contain identifiers and other information.

**Sessions:**
- Allow servers to store user-specific information across multiple requests.
- A session identifier is commonly stored in a browser cookie.
- The server uses this identifier to retrieve the corresponding session data.

For example, login systems use sessions to remember that a user is authenticated.

### 8. Explain how Django handles a request using URLs, views, models, and templates.

Django follows the Model-Template-View (MTV) architectural pattern.

The request flow is:

1. A user sends a request to the Django application.
2. Django's URL dispatcher checks the project's URL configuration.
3. The request is routed to the appropriate app URL configuration, if included.
4. The URL configuration maps the requested path to a view.
5. The view processes the request and interacts with models when database access is required.
6. Models represent database data and allow the application to retrieve or modify it using Django's ORM.
7. The view passes the required data to a template.
8. The template generates HTML using the provided context.
9. Django returns an HTTP response to the browser.

In this polling application, the index view retrieves questions from the database, passes them to the index template, and returns the rendered HTML to the browser.

### 9. Why is `{% csrf_token %}` added to the voting form?

CSRF stands for Cross-Site Request Forgery.

It is an attack in which a malicious website attempts to trick an authenticated user's browser into sending an unwanted request to another website.

Django provides CSRF protection using a token.

The `{% csrf_token %}` template tag inserts a hidden token into the form. When the form is submitted, Django checks the token to verify that the request originated from a page that has the appropriate CSRF token.

In this polling application, the voting form uses POST, so including `{% csrf_token %}` helps protect the voting endpoint against CSRF attacks.

## Technologies Used

- Python
- Django
- SQLite
- HTML
- Git and GitHub

## Project Repository

[GitHub Repository](https://github.com/codeman2008/poll)
