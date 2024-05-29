from api_ig import get_data_instagram
from datetime import datetime
import pandas as pd


def new_data():
    df_excel = pd.read_excel('date_pages.xlsx')
    pages = ['cs2nicetry' , 'draft5gg' , 'fallendadepre' , 'theclutchcsgo' , 'dust2_br' , 'cs.br.oficial']
    data_list = []
    for page in pages:
        json_data = get_data_instagram(page)
        data_dict = {
        'followers' : json_data['followers_count'],
        'name' : json_data['name'],
        'username' : json_data['username'],
        'website' : json_data['website'],
        'url_photo' : json_data['profilepicture_url'],
        'date' : datetime.today()
    }
    data_list.append(data_dict)
    df_api = pd.DataFrame(data_list)
    df_final = pd.concat([df_excel, df_api], ignore_index=True)
    df_final.to_excel('date_pages.xlsx', index=False)

