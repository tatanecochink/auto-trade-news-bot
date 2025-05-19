import requests

def lire_nouvelle():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "économie",
        "apiKey": "6811ae98a9554ae490eae22d1ad9ca37"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["articles"]:
            titre = data["articles"][0]["title"]
            print("Nouvelle principale :", titre)
        else:
            print("Aucune nouvelle trouvée.")
    else:
        print("Erreur lors du chargement des nouvelles :", response.status_code)

lire_nouvelle()