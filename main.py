import requests

# User input
word = input("Enter Word: ")

# url/api to fetch results
url = 'https://api.dictionaryapi.dev/api/v1/entries/en/' + word

# Sending GET request 
r = requests.get(url)

# Extracting data in json format 
result = r.json()
print('\n' "*************************************" )

# Try / evalute : results found
try:
  data = result[0]
  print('Results for :' + ' ' +  data['word'])
  print("Pronounced: {}".format(data['phonetic']))
  print("-------------------------------------")

  count = 1

  # Getting meaning(s) of the word
  for means in data['meaning']:
    print('Definition No.{}:'.format(count))
    count = count + 1
    print('\u0332'.join(means) + ' : ' + data['meaning'][means][0]['definition'] + '\n')
    
    # Getting example(s)
    if 'example' in  data['meaning'][means][0]:
      print('Example : ' + data['meaning'][means][0]['example'])
      print("-------------------------------------\n")
  

# If results not found
except Exception:
  print("No results found!")


print("*************************************" '\n')