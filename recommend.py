import webbrowser
from dotenv import load_dotenv

load_dotenv()

from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk
import cred
import spotipy



def open_spotify(url):
    webbrowser.open(url, new=2)


def create_label(text):
    return tk.Label(master=frm_recommendations, text=text)


def create_button(text, url):
    return tk.Button(master=frm_recommendations, text=text, command=lambda: open_spotify(url))


def clear(*args):
    args.destroy()


def display_recommendations(response):
    lbl_track_name = tk.Label(master=frm_recommendations, text='Track Name')
    lbl_artist_name = tk.Label(master=frm_recommendations, text='Artist Name')
    lbl_play_it = tk.Label(master=frm_recommendations, text='Play it')
    lbl_track_name.grid(row=0, column=0)
    lbl_artist_name.grid(row=0, column=1)
    lbl_play_it.grid(row=0, column=2)
    for idx, track in enumerate(response['tracks']):
        lbl_track_name_recommended = create_label(track['name'])
        lbl_track_name_recommended.grid(row=idx + 1, column=0)
        lbl_artist_name_recommended = create_label(track['artists'][0]['name'])
        lbl_artist_name_recommended.grid(row=idx + 1, column=1)
        btn_play_it_recommended = create_button('Play It', track['external_urls']['spotify'])
        btn_play_it_recommended.grid(row=idx + 1, column=2, padx=10)


def get_recommendations():
    search = ent_search.get()
    ID=cred.client_ID
    KEY=cred.client_SECRET
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(ID,KEY))
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url))
    result = sp.search(q=search, limit=1)
    id_list = [result['tracks']['items'][0]['id']]
    recommendations = sp.recommendations(seed_tracks=id_list, limit=10)
    display_recommendations(recommendations)


window = tk.Tk()
frm_search_field = tk.Frame(master=window, width=100)
frm_recommendations = tk.Frame(master=window)
window.title("Mr.R")
p1 = tk.PhotoImage(file='./icon/recommendation.png')
window.iconphoto(False, p1)
# window['background']='#2B4063'

frm_search_field.pack()
frm_recommendations.pack()
ent_search = tk.Entry(master=frm_search_field, width=25)
btn_get_recommendations = tk.Button(master=frm_search_field, text=' Get Recommendation', command=get_recommendations)
ent_search.grid(row=0, column=0, padx=10, pady=10)
btn_get_recommendations.grid(row=0, column=1, padx=10, pady=10)
window.mainloop()
