# Django Todo list App
This Django Application primarily focusses on developing a todolist through the django rest framework functionality. The TODO list APIs have multiple implementations of the same request types using different methods such as POST using Generic class based views versus traditional REST APIs.  

Any generic class based view apis will allow all CRUD functionality to be done in one API using different request types as headers, while the traditional apis have different endpoints for each request type.  

## TODO List APIs: 

  **Authetication (DRF Based):** 
  - Log In: /auth/login/ 
  - Log Out: /auth/logout/ 

  **Authetication (Default Django Based):** 
  - Log In: /accounts/login/ 
  - Log Out: /accounts/logout/ 

  **Traditional REST APIs:** 
  - Task List : api/task/all, 
  - Task-Retrieve: api/task/view/<str:pk>, 
  - Task-Create: api/task/create, 
  - Task-Update: api/task/update/<str:pk>, 
  - Task-Delete: api/task/delete/<str:pk>, 

  **Task List Generic Class Based Views APIs:** 
  - Task_CRUD: api/task/<str:pk> 
  
  **User Generic Class Based Views APIs:**  
  - User-List: api/user/, 
  - User-Retrieve: api/user/<int:pk> 

