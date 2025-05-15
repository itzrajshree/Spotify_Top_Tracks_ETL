from spotipy.oauth2 import SpotifyOAuth

sp_oauth = SpotifyOAuth(
    client_id="723b1714cc9740e2b396a431374dec93",
    client_secret="173d8d47198146b0a27cffcdaf3a6ba3",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-top-read"
)

token_info = sp_oauth.get_access_token(as_dict=True)
print("Access token:", token_info['access_token'])
print("Refresh token:", token_info['refresh_token'])
