# Flask Post App

Flask Post App is a web application built with Flask, a Python web framework. It allows users to create, read, update, and delete blog posts.

## Features

- Create new blog posts
- View a list of all blog posts
- View details of a specific blog post
- Update an existing blog post
- Delete a blog post

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-post-app.git
```

2. Navigate to the project directory:

```bash
cd flask-post-app
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
```

```bash
source venv/bin/activate # On MacOs
```

```bash
venv\Scripts\activate # On Windows
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, you need to configure the following environment variables:

- `SECRET_KEY`: A secret key for securely signing the session cookie.
- `DATABASE_URL`: The URL for the database connection.

You can set these environment variables in a `.env` file in the project root directory or export them in your shell.

## Running the Application

To run the Flask Post App, execute the following command:

```bash
flask run
```

This will start the development server, and you can access the application at `http://localhost:5000`.

## Usage

1. **Create a new post**: Navigate to `/create` and fill out the form to create a new blog post.
2. **View all posts**: Visit the homepage (`/`) to see a list of all blog posts.
3. **View a specific post**: Click on the title of a post in the list to view its details.
4. **Update a post**: On the post detail page, click the "Edit" button to update the post's content.
5. **Delete a post**: On the post detail page, click the "Delete" button to remove the post.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

This documentation provides an overview of the Flask Post App, including its features, installation instructions, configuration steps, usage guide, and information about contributing and licensing. You can customize and expand this documentation as needed based on your specific application requirements.
