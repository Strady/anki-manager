import requests

from anki_client.constants import Fields, URL

CSS = """.card {
    font-family: arial;
    font-size: 20px;
    line-height: 1.5;
    text-align: center;
    color: black;
    background-color: white;
}"""
FRONT_TEMPLATE = '{{Text Front}}<hr>{{Audio Front}}'
BACK_TEMPLATE = """{{Image}}
<hr>
{{Audio Back}}
<hr>
<div style="text-align: justify;">{{Text Back}}</div>
<hr>
<div style="text-align: justify;">Example: {{Text Example}}</div>
"""


body = {
  'action': 'createModel',
  'version': 6,
  'params': {
    'modelName': MODEL_NAME,
    'inOrderFields': Fields.as_tuple(),
    'css': CSS,
    'cardTemplates': [
      {
        'Name': 'FalloutNote',
        'Front': FRONT_TEMPLATE,
        'Back': BACK_TEMPLATE
      }
    ]
  }
}

response = requests.post(url=URL, json=body)
print(response, response.text)
