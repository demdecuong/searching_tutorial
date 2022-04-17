import urllib.request
import gzip
import io
import json
import pandas as pd

df = pd.read_csv('data/oganization.csv')

for index, row in df.iterrows():
    print(row['c1'], row['c2'])
    
# with urllib.request.urlopen(url_get) as response:
#     encoding = response.info().get_param('charset', 'utf8')
#     compressed_file = io.BytesIO(response.read())
#     decompressed_file = gzip.decompress(compressed_file.read())
    # json_str = json.loads(decompressed_file.decode('utf-8'))