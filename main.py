import requests
import json
import pandas as pd

from keboola_config import Configuration

kb_config = Configuration()

###setup###

app_id = kb_config.app_id
table_id = kb_config.table_id
merge_on_field = kb_config.column_name
bearer_api_token = kb_config.token
url = "https://api.airtable.com/v0/" + str(app_id) + '/' + str(table_id)

###payload setup###
data = pd.read_csv('in/tables/test.csv') #in/tables/

records = [
    {"fields": row.to_dict()}
    for _, row in data.iterrows()
]

payload = json.dumps({
    "performUpsert": {
        "fieldsToMergeOn": [
            merge_on_field
        ]
    },
    "records": records
})

headers = {
    'Authorization': 'Bearer ' + str(bearer_api_token),
    'Content-Type': 'application/json'
}

###API call###
response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
