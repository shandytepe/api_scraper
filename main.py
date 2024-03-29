import pandas as pd
import requests
from tqdm import tqdm
import time
from src.utils import current_time

def scrape_ggwp_api(num_of_page):
    """
    Function yang digunakan untuk scrape data menggunakan GGWP API

    Parameters
    ----------
    num_of_page (int): Jumlah halaman yang ingin discrape

    Returns
    -------
    data (list): List of json atau list of dictionary data yang sudah discrape
    """
    data = []

    for page in tqdm(range(1, num_of_page + 1)):
        resp = requests.get(f"https://tourney-api.ggwp.id/api/v2/media/getLatestArticle?page={page}")

        raw_response = resp.json()

        if raw_response["success"] == False:
            break

        get_data = raw_response["data"]["data"]

        data.extend(get_data)

        time.sleep(0.5)

    return data

def save_output(data, filename):
    """
    Function yang digunakan untuk mengubah data menjadi DataFrame dan
    menyimpan data menjadi format csv

    Parameters
    ----------
    data (list): List of dictionary berisi data yang sudah discrape pada proses sebelumnya
    filename (str): Filename yang digunakan untuk menyimpan data scrape 
    """
    data = pd.DataFrame(data)

    data["scraped_at"] = current_time()

    data.to_csv(filename, index = False)

if __name__ == "__main__":
    OUTPUT_PATH = "data/"

    print("========== START DATA SCRAPE ==========")

    # 1. start scrape API
    api_data = scrape_ggwp_api(num_of_page = 20)

    # 2. save the output into csv
    save_output(data = api_data,
                filename = OUTPUT_PATH + "ggwp_data.csv")
    
    print("========== END DATA SCRAPE ==========")