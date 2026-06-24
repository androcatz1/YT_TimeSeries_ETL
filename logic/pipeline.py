from etl.extract import (
    get_video_ids_since_date,
    fetch_video_metadata
)
from config.settings import Settings
from etl.load import insert_to_bigquery

if __name__ == "__main__":
    all_video_ids = []

    for channel_id in Settings.CHANNEL_IDS:
        ids = get_video_ids_since_date(channel_id)
        all_video_ids.extend(ids)

    rows = fetch_video_metadata(all_video_ids)

    insert_to_bigquery(rows)