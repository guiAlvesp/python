import requests

repo_list = []

nome = str(input("por favor, insira seu usuario do github:  "))
if nome == '':
    print("por favor, insira seu usuario do github")
    nome = str(input("por favor, insira seu usuario do github:  "))


r = requests.get(f'https://api.github.com/users/{nome}/repos')
repo = r.json()



for repos in repo:

    repo_list.append(repos['name'])
    print(repo_list)