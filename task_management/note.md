
Task Management System

You are asked to implement a Django ‘Task Management System’ project where anyone can add a task under different categories, edit the tasks, and delete the tasks. You need to create a model i.e 

‘TaskModel’ having fields 
taskTitle 
taskDescription 
is_completed by default False
Task Assign Date
N.B : Here ‘is_completed’ field should be of type models.BooleanField and default values for this field should be ‘False’                                                            

TaskCategory Model will have
Category Name
Many-to-Many Relationships with task model                              

In this project, users should be able to: 
Add a navigation bar where user will see Add Task,Add Category, Show Tasks menu 
In the Show Tasks Page users can see all the tasks in bootstrap card style, for every task there will be two buttons Edit Delete  . For completed tasks the user won’t see the edit and delete button rather see Completed. 
An User can edit the task, delete the task, complete the task. When a task is completed then the is_completed will be True.                               
In the Add Task Page, users can see a form based on the task model form, can provide title, description, can select multiple categories, Is Completed and then submit the form and the data must be added to the database and then redirect the user to the Show Tasks page. You must use the model form here.
In the Add Category page, users can add a category by its name. Use model form here 
Following requirements must be filled : 
There must be two apps named task and category
Global templates for base.html and and app templates for showing forms in both apps


________________________________________________________________________________
|  _________________    _____________        _______________    _____________   |
| |                 |  |            |       |               |   |           |   |
| | Task Management |  | Add Task   |       | Add Category  |   | Show Task |   |
| |_________________|  |____________|       |_______________|   |___________|   |
|_______________________________________________________________________________|
|                                  Show Task                                    |                    
|                                                                               |          
|        ____________________________     _________________________________     |
|       |                            |   |                                  |   |
|       |                            |   |                                  |   |
|       |       Task ID              |   |           Task ID                |   |
|       |     Task Assigned Date     |   |         Task Assigned Date       |   |
|       |     Task Description       |   |          Task Description        |   |
|       |       Task Category        |   |          Task Category           |   |
|       |       Edit / Delete        |   |              complated           |   |
|       |____________________________|   |__________________________________|   |   
|                                                                               |
|       ______________________________    ___________________________________   |
|       |                            |   |                                   |  |
|       |                            |   |                                   |  |
|       |       Task ID              |   |      Task ID                      |  |
|       |     Task Assigned Date     |   |      Task Assigned Date           |  |
|       |     Task Description       |   |      Task Description             |  |
|       |       Task Category        |   |      Task Category                |  |
|       |       Edit / Delete        |   |      complated                    |  |   
|       |____________________________|   |___________________________________|  |
|_______________________________________________________________________________|   





________________________________________________________________________________
|  _________________    _____________        _______________    _____________   |
| |                 |  |            |       |               |   |           |   |
| | Task Management |  | Add Task   |       | Add Category  |   | Show Task |   |
| |_________________|  |____________|       |_______________|   |___________|   |
|_______________________________________________________________________________|
|                                  Add Task                                     |                    
|                                                                               |          
|        __________________________________________________________________     |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |   
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |   
|       |__________________________________________ ________________________|   |
|_______________________________________________________________________________|   



________________________________________________________________________________
|  _________________    _____________        _______________    _____________   |
| |                 |  |            |       |               |   |           |   |
| | Task Management |  | Add Task   |       | Add Category  |   | Show Task |   |
| |_________________|  |____________|       |_______________|   |___________|   |
|_______________________________________________________________________________|
|                                  Add Category                                 |                    
|                                                                               |          
|        __________________________________________________________________     |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |   
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |
|       |                                                                   |   |   
|       |__________________________________________ ________________________|   |
|_______________________________________________________________________________|   






