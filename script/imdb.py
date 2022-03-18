# %% [markdown]
# # Coletando dados do Imdb

# %%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import mysql.connector as mdb

# %% [markdown]
# Coletando dados das séries mais aguardadas de 2022

# %%
con = mdb.connect(user='root', password='113283Tt&', database='transfermarkt')

# %%
cursor = con.cursor()

# %%
#cursor.execute("CREATE DATABASE IMDb")

# %%
cursor.execute("USE IMDb")

# %%
#cursor.execute("CREATE TABLE series2022 (Serie TEXT NOT NULL, Popularidade TEXT NOT NULL)")

# %%
url = ['https://www.imdb.com/title/tt11198330/?ref_=nv_sr_srsg_3', 'https://www.imdb.com/title/tt7631058/?ref_=nv_sr_srsg_1', 'https://www.imdb.com/title/tt3581920/?ref_=nv_sr_srsg_0', 'https://www.imdb.com/title/tt2934286/?ref_=nv_sr_srsg_0', 'https://www.imdb.com/title/tt10234724/?ref_=nv_sr_srsg_0',
       'https://www.imdb.com/title/tt8466564/?ref_=nv_sr_srsg_0', 'https://www.imdb.com/title/tt1751634/?ref_=nv_sr_srsg_0', 'https://www.imdb.com/title/tt10857160/?ref_=nv_sr_srsg_3', 'https://www.imdb.com/title/tt12785720/?ref_=nv_sr_srsg_3', 'https://www.imdb.com/title/tt11311302/?ref_=nv_sr_srsg_3']

# %%
url

# %%
url[0]

# %%
Serie = []
Popularidade = []
for i in range(0, 10):
    field = {}
    html = requests.get(url[i])
    html_page = html.text
    soup = BeautifulSoup(html_page, 'lxml')
    S = soup.find_all(
        "h1", attrs={'class': 'TitleHeader__TitleText-sc-1wu6n3d-0'})[0].text
    field['Série'] = S
    P = soup.find_all(
        "div", attrs={'class': 'TrendingButton__TrendingScore-sc-bb3vt8-1'})[0].text
    field['Popularidade'] = P
    Serie.append(field)
    Popularidade.append(P)
    insertIMDb = ("INSERT INTO series2022 (Serie, Popularidade) values ('%s', '%s')" % (
        Serie, Popularidade))

# %%
con.commit()

# %%
Serie = []
for i in url:
    field = {}
    html = requests.get(i)
    html_page = html.text
    soup = BeautifulSoup(html_page, 'lxml')
    S = soup.find_all(
        "h1", attrs={'class': 'TitleHeader__TitleText-sc-1wu6n3d-0'})[0].text
    field['Série'] = S
    Serie.append(S)

# %%
Serie

# %%
field

# %%
html = requests.get(url[1])
html_page = html.text
soup = BeautifulSoup(html_page, 'lxml')
S = soup.find_all("h1", attrs={'class': 'TitleHeader__TitleText-sc-1wu6n3d-0'})

# %%
S

# %%
html = requests.get(url[1])

# %%
html

# %%
html_page = html.text

# %%
html_page

# %%
soup = BeautifulSoup(html_page, 'lxml')

# %%
soup

# %%
S = soup.find_all("h1", attrs={'class': 'TitleHeader__TitleText-sc-1wu6n3d-0'})

# %%
S

# %%
url[1]

# %%
