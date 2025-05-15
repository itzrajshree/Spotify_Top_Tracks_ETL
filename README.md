# 🎧 Spotify ETL Pipeline

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline that pulls data from the Spotify Web API, performs data quality checks, and loads the cleaned data into a PostgreSQL database. The goal is to track and analyze your personal top tracks on Spotify.

---

## 🚀 Features

- Extracts top tracks using Spotify Web API (short-term, medium-term, or long-term)
- Transforms data to retain relevant fields (track name, artist, album, duration, popularity, etc.)
- Data quality checks:
  - Ensures no `NULL` values in critical fields
  - Checks and removes duplicate `track_id`s
- Loads clean data into a PostgreSQL table
- Data is visualized using DBeaver

---

## 📦 Tech Stack

- **Python** – Scripting and data processing  
- **Spotify Web API** – Data extraction  
- **PostgreSQL** – Data storage  
- **DBeaver** – SQL client for table visualization  
- **Libraries**: `requests`, `psycopg2`, `pandas`, `dotenv`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/spotify-etl-pipeline.git
cd spotify-etl-pipeline
````

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your Spotify and PostgreSQL credentials:

```env
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback

DB_HOST=localhost
DB_PORT=5432
DB_NAME=spotify_etl
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

---

## 🧪 Running the ETL Pipeline

Run the main script:

```bash
python etl.py
```

The script will:

* Authenticate using Spotify credentials
* Fetch your top tracks
* Clean the data by checking for null values and duplicate `track_id`s
* Load the cleaned data into a PostgreSQL table

---

## 🗃️ Database Schema

**Table Name:** `Top_tracks`

| Column Name  | Data Type | Description                   |
| ------------ | --------- | ----------------------------- |
| track\_id    | TEXT      | Unique ID of the track        |
| track\_name  | TEXT      | Name of the track             |
| artist\_name | TEXT      | Primary artist                |
| album\_name  | TEXT      | Album the track belongs to    |
| duration\_ms | INTEGER   | Duration in milliseconds      |
| popularity   | INTEGER   | Track popularity (0–100)      |
| added\_at    | TIMESTAMP | Timestamp when data was added |

---

## 📊 Output

Once the data is loaded, you can use DBeaver or any other SQL client to inspect the table:

```sql
SELECT * FROM Top_tracks;
```

You’ll see your top tracks with all relevant fields, cleaned and ready for analysis.

---

## 📸 Screenshots

> Spotify DAG: Spotify_DAG.png
> Spotify Top Tracks Table in DBeaver: Spotify_Top_Tracks.png

---

## 📌 To-Do / Possible Enhancements

* [ ] Load additional features (e.g., genres, audio features like tempo, danceability)
* [ ] Automate ETL using Airflow or Prefect
* [ ] Historical data tracking for trend analysis
* [ ] Add unit tests and logging

---

## 📝 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for more details.

---

## 🙋‍♀️ Author

**Rajshree**
📧 Feel free to connect or check out more of my projects!
🔗 \[Your LinkedIn / Portfolio / GitHub URL here]

```

Let me know if you'd like help adding images, badges, or a `requirements.txt` file!
```
