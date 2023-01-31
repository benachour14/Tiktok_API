import requests
import math as Math
import random , string

redirect_uri= "https://oauthdebugger.com/debug"
response_type='code'
client_id="awi1zy45ku8ss868"
scope="user.info.basic,video.list"
state = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=30))

# Construire l'URL de demande d'autorisation
url = f'https://www.tiktok.com/auth/authorize/?client_key={client_id}&response_type={response_type}&scope={scope}&redirect_uri={redirect_uri}&state={state}'

# Afficher l'URL
print(url)
