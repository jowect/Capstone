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
export ALGORITHMS = 'RS256'
export API_AUDIENCE = 'movie' 
# for local database use database_path with your local database URI
# export DATABASE_URL = database_path
export DATABASE_URL = 'postgres://wqlwqncscphcfx:3e859ca1b5ec222029233138067b706303f74ac2c287d2a1d892bb086f8156ab@ec2-54-163-47-62.compute-1.amazonaws.com:5432/dvfahj6moq3cs'
export jwt_exec_prod = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4NDNiM2NiZWI2MmIwMDY4ZTI1OGI2IiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ2OTUsImV4cCI6MTYwNjIyMTA5NSwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.LLrh-UGj0DWCJBowOjEfKTcHo1Gx7AEah_XsJUK5Sg6nTHHIYvGJ3YGSt7HQZ5F20AaKMMO66cxwFy-dyZ2OyZ7W7C9cLLcibCVP3OZkZjImzYqlEnyuDZNG_o7xzTHOj7VU8NXaPEy7fF81DzdSdH692znLmgrUIWPdIuBkwuMr3aPhVENMuI0pSWQVI1ivnioey4jTccOGrSQtdkgbDoa6E0TB8HENlPa3HmqLHar04vMfbWLeSN2Qew1-UgkLWIc6J7jRkNo-LUpdcBb7GXhZ3Hn2jZdItYdz9dV3-P0l1zA8PhrQ_PT-D_WsvqxLUb95L1GfaerBQ0JV1gqQyw'
export jwt_cast_dir = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZiNTIyODJhYTY3YjIwMDc1OTA5OTc0IiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ4OTIsImV4cCI6MTYwNjIyMTI5MiwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.zMvXctru3e_FN3L-XyPbzEss_a5faAeu7XwlPuhJJnAtMgEkNN9XoNCrbJa6Jba-2-jTbg4aSMcUhB6vfOLPYp9wnKk2YDFpW-X6AEzN2-RbUfnpIHsjtPjeXeLlDLO17C9yzQgVH9f1nVej9mhgk-jpyytoFvFTdpslm7WBbMXRv2XnVYb4R0tfSzO0xn6fWvyzRYZzAgsmWGnFqTm3UnL3i51K_tIinXC1rsxYSfQ9_o-R-P6gFOgu74iKt8CRlKf5wRA2lhZZx8Xm-_-bRVJU3nJ3Ar8AjAZwYpC2xrLZ91G8t1C0d3DA0kctZvtWvyo6ZAbJESsrC71QJE1FXA'
export jwt_cast_as = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtuaUE2aGR1Z3I1Ulc4bmRoTDhScCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqdy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4OGE0OWRmYjFmNzAwMDc2YWU3ZWMzIiwiYXVkIjoibW92aWUiLCJpYXQiOjE2MDYxMzQ4MjEsImV4cCI6MTYwNjIyMTIyMSwiYXpwIjoiVjFyaVRKWmhsWjRiNFBpQ3FibG5kOFNqTFJEV2lsU3AiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDpzZWFyY2hBY3RvcnMiLCJwb3N0OnNlYXJjaE1vdmllcyJdfQ.sJfQ0cPRJtQQrP36fwkafoYpwekjZIEiYiLgT_aGUfWSeAHEB_kEGrZSct42Bimh7Y_nNasmgw0QbB9Ux4p3eOnEgM9bIKfr38yA3IBDvufM0bhVzv_pz6BHy3husfslpZYO_QtyJgGWQtFDpm_65jNzh6dsk7DuJRheeuml5Cj4SMDLB__hpSfof03HlEsgS3VPqXEa8acwSgKsCiCQpTGrrzjjQKoqmR2S8q7V_bvwB8sAyNV3ZMWTnHF7JVgGRt2lHMxmw1x8x4pWYEZ4So99U1OyNIJc1lcfEPfvDIggU0BR8VPXKre_3D5FNc7lDCYLrskXGdAYLiwthVijxw'
