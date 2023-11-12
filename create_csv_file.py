import json
import csv
import pandas as pd
from sklearn.utils import resample


def json_to_csv():
    jsonFile = input("Lutfen cevirmek istediginiz json dosyasinin adini giriniz: ")
    csvFile = input("Csv dosyanizin adini giriniz: ")
    csvFile += ".csv"
    with open(jsonFile,'r',encoding='utf-8') as json_file:
        data = json.load(json_file)
    with open(csvFile,'w',encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data[0].keys())

        for row in data:
            csv_writer.writerow(row.values())
    print("Csv Dosyası oluşturuldu")
def csv_to_dataframe(csvFile= "tum_sarkilar.csv"):
    # csvFile = input("Csv dosyanizin adini giriniz: ")
    # csvFile += ".csv"
    df_song = pd.read_csv(csvFile)
    return df_song

def csv_info(df_song):
    print("Dataframe'in veribilgileri: ")
    print(df_song.info())
    print("Dataframe'de toplamda bulunan boş alanlar: ")
    print(df_song.isna().sum())
    print("Datafram'de bulunan sınıfların sayısı: ")
    df_graph = pd.DataFrame({
        "Sınıflar": df_song["class"].value_counts().index,
        "Miktarlar": df_song["class"].value_counts().values
    })
    print(df_graph)
    print("Datafram'de bulunan sınıfların sayısının grafikleri: ")







########## PROGRAM ##########
# json_to_csv()
df_song = csv_to_dataframe(csvFile="test.csv")
csv_info(df_song)


