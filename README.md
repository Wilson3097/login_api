# Login_api
  A basic django rest API for basic registration and authentication.
  
  ## Steps to run the server:
1. Install all the requirements from the requirements.txt file by running the following command:
    - pip install requirements.txt
2. To run the server type the following command:
    - python manage.py runserver
  
 ## APIs documentation
 ### User Authorization Endpoints
      
   <table>
    <tr>
        	<th>S.No.</th>
   		<th>Route</th>
   		<th>Method</th>
   		<th>Access</th>
   		<th>Description</th>
   	</tr>
   	<tr>
           <td>1.</td>
           <td>api/register/</td>
           <td>POST</td>
           <td>public</td>
           <td>Enter the details to create an user</td>
       </tr> 
       <tr>
           <td>2.</td>
           <td>api/login/</td>
           <td>POST</td>
           <td>private</td>
           <td>Enter the credentials to login</td>
       </tr> 
    </table>
