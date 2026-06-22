import requests
r = requests.get('https://api.github.com/users/codewithharry') 
print(r.text)
with open("codeharry","w") as f:
    f.write(r.text)