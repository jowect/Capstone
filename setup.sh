url: 'fsndjw.eu',
#  // the auth0 domain prefix
audience: 'movie',
    #  // the audience set for the auth0 app
clientId: 'V1riTJZhlZ4b4PiCqblnd8SjLRDWilSp',
    #  // the client id generated for the auth0 app
callbackURL: 'http://127.0.0.1:8080', 
    # // the base url of the running ionic application. 

database_name = 'heroku_test'
user_name = 'postgres'
user_password = 'w1zu'
host = 'localhost:5432'
database_path = "postgres://{}:{}@{}/{}".format(user_name, user_password, host, database_name)

export AUTH0_DOMAIN = 'fsndjw.eu.auth0.com'
export ALGORITHMS = ['RS256']
export API_AUDIENCE = 'movie' 
# for local database use database_path with your local database URI
#export DATABASE_URL = database_path
export DATABASE_URL = 'postgres://wqlwqncscphcfx:3e859ca1b5ec222029233138067b706303f74ac2c287d2a1d892bb086f8156ab@ec2-54-163-47-62.compute-1.amazonaws.com:5432/dvfahj6moq3cs'