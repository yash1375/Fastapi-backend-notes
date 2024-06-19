#  Notes Backned
## Backend using Fastapi + Mongodb

### Feature
1. **CRUD**(Create,Read,Update,Delete,) Opration On **NOTES**
2. User Signup and login
3. JWT Based Login
4. Encryption Password for Security (Trust me i will not read your email)

## HOW TO USE

1. Clone Repo
2. open Terminal in Clone repo dict
3. Install requirements.txt `pip install -r requirements.txt` 
4. fastapi dev start.py

## Route - All value in Json
1. ## For create User - http://127.0.0.1:8000/user/createuser  (POST)
### Required Body Value
1. username
2. password
3. email
4. Date -optional (Will Take Current Time)

2. ## For Login User - http://127.0.0.1:8000/user/login (GET)
### Required Body Value
1. username
2. password
#### WIll return auth_token

3. ## For Fetch user info - http://127.0.0.1:8000/user/getuser NO login Required (GET)
### Required Body Value
1. username
2. password
### Required Header
1. auth-token 
#### WIll return user info

4. ## For create Note info - http://127.0.0.1:8000/note/createnote NO login Required (POST)
### Required Body Value
1. Title
2. Desc
3. Tag -default vale Gen
4. Date -optional (Will Take Current Time)
### Required Header
1. auth-token 

5. ## For Fetch All Note of a User - http://127.0.0.1:8000/note/fetchnote NO login Required (GET)
### Required Header
1. auth-token 

6. ## For Update Note of a User - http://127.0.0.1:8000/note/updatenote/<id> NO login Required (PUT)
### Required Path
1. id (Notes id)
### Required Body Value
Any Value u need to update
### Required Header
1. auth-token 

7. ## For Delate Note of a User - http://127.0.0.1:8000/note/deletenote/<id> NO login Required (DELETE)
### Required Path
1. id (Notes id)
### Required Header
1. auth-token 

