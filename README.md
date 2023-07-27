<br>
<h1 align="center">⭐️ Restful_Api ⭐️</h1>

<h2 align="center">Hi , I'm Delphine  👋</h2>  

<h3 align="center">This repository is a python exercise carried out during Becode training   </h3> <br>

* <h2 align="left"> Introduction</h2> 

>Create an API to share data with other companies.
>Create a database called api and a table called posts with the following fields.
The url of the API will be for example: http://localhost:8000/api/v1/posts

<h2 align="left">📦 Prerequisites</h2> 
<br>
Before you begin, please ensure that you have the following items installed on your machine:

1. Programming language (python 3)
2. Web server ()
3. Database management system (e.g. MySQL)

<br>

<h2 align="left">🚀 Installation</h2>

1. Clonez ce dépôt de code sur votre machine locale :


* Clone the Repository
  ```sh
    git clone https://github.com/your-username/restful-api-flask.git
  ```
  
	```sh
	  cd restful-api-flask
	```

* Create a Virtual Environment (optional):
  ```sh
 	python -m venv venv
  ```

	```sh
	  source venv/bin/activate # For Windows, use 	"venv\Scripts\activate"
	```

* Install Dependencies:
  ```sh
    pip install -r requirements.txt
  ```

* Set Environment Variables:
  ```sh
    SQLALCHEMY_DATABASE_URI=mysql+pymysql://your_username:your_password@localhost/api

  ```

* Run the Flask App:
 	```sh
 	python app.py
	```

The API will now be accessible at http://127.0.0.1:5000/api.


<br>
<h2 align="left">Objectives </h2>

>Create an API to share data with other companies.
>>

<br>

📝 Model : <br> 
>> This directory contains the classes and functionalities linked to the application's data and business logic. <br>This includes communication with the database, CRUD (Create, Read, Update, Delete) operations and everything else relating to the data.<br>

📝 Controller : <br>
>> This directory contains the classes which act as intermediaries between the model and the view. <br>Controllers are responsible for receiving user requests, coordinating the necessary model actions and rendering the appropriate view with the corresponding data.<br>

<br>

📝 Endpoints
The following endpoints are available for the posts resource:

>GET /api/v1/posts: Get all posts.
GET /api/v1/posts/{id}: Get a specific post by ID.
POST /api/v1/posts: Create a new post.
PUT /api/v1/posts/{id}: Update a post by ID.
DELETE /api/v1/posts/{id}: Delete a post by ID.
<br>
📝 Usage

>To use the API, you can send HTTP requests to the endpoints mentioned above using tools like cURL or Postman. Below is an example of using cURL to create a new post:

<h3>HTTP response status codes indicate whether a specific HTTP </h3>

<h4>Status Code: 200</h4>

>Description: The request was successful, and the server has returned the requested data.
Usage in Code: Returned when a post is successfully deleted from the database. It indicates that the deletion process was successful, and the post was removed.

<h4>Status Code: 201</h4>

>The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.

<h4>Status Code: 400</h4>

>The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).

<h4>Status Code: 404 </h4>

>Not Found
Description: The server could not find the requested resource.
Usage in Code: Returned when attempting to delete a post with an ID that does not exist in the database. It indicates that the post was not found and, therefore, cannot be deleted.

<h4>Status Code: 500</h4>

>Description: The server encountered an unexpected condition that prevented it from fulfilling the request.
Usage in Code: Returned if there is an error during the deletion process that is not expected or handled explicitly. This could include database errors or other unexpected exceptions.

https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

<h2 align="left">💻 Tech Stack</h2>  

<p align='left'>
  
<img src="https://github.com/DelphineLecorney/Template-readme/blob/main/PICTURES_read_me_/visual-studio.jpg" alt="VSCode" height="60" width="60" />

<img src="https://github.com/DelphineLecorney/Template-readme/blob/main/PICTURES_read_me_/myphpadmin.png" alt="phpmyadmin" height="60" width="60" />   
 
<img src="https://github.com/DelphineLecorney/photos-images-readme/blob/main/images/python.png" alt="Python"/>

</p>
<h2 align="left"> Contact me : </h2> <a href="https://www.linkedin.com/in/delphine-lecorney/" target="_blank"><br /><sub><b>Delphine</b></sub>

