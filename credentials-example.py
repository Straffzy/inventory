# ========================================================= #
#                Example credentials.py file                #
#  Before using, make a copy and rename to "credentials.py" #
#    ---> add credentials.py to your .gitignore file <---   #
# ========================================================= #


# Django Secret Key
django = { 
        'secret_key' : 'paste your secret key here'
        }

# In settings.py, do the following (remove comment #s)

# This line goes before the SECRET_KEY line
# or can be placed at/near the top of the file  

# import credentials 

# This line replaces the SECRET_KEY line AFTER you paste
# the secret key into this file, above

# SECRET_KEY = credentials.django['secret_key'] 

# ============================================ #
