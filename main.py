import requests

def lire_nouvelle():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "ca",
        "apiKey": "INSÈRE_TA_CLÉ_API_ICI"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        titre = data["articles"][0]["title"]
        print("Nouvelle principale :", titre)
    else:
        print("Erreur lors du chargement des nouvelles :", response.status_code)

lire_nouvelle()