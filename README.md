# BiquestAPI
A bible quiz Api with Python Django

## Admin URL
https://biquest.herokuapp.com/admin

## Admin Access Credentials
- Username: folajimi
- Password: **************


## API ENDPOINTS - 1
- https://biquest.herokuapp.com/api/quiz/

- Request Type: GET
- Data Description: The above endpoint fetches n=10 questions at random from all quiz question in the database

## API ENDPOINTS – 1 with query
- https://biquest.herokuapp.com/api/quiz/?rand=20

- Request Type: GET
- Data Description: At default /api/quiz/ endpoint returns 10 questions, the query ?rand=20, allows developer to specify a particular number of random questions that should be fetched could be less than or greater that the default 10 (i.e. 10 < n > 10).

- JSON format: success 
- Status: <p style="color: green;">200 OK</p>
