from database.connection import get_connection


def insert_to_bigquery(rows):
    client = get_connection()
    table_id = "vaulted-bonsai-487010-t7.youtube.video_metrics_time_series"

    payload = [
        {
            "video_id": r[0],
            "title": r[1],
            "description": r[2],
            "tags": r[3],
            "category_id": r[4],
            "channel_title": r[5],
            "published_at": r[6],
            "views": r[7],
            "likes": r[8],
            "comments_count": r[9],
            "platform": None,  
            "fetched_at": r[11].isoformat() if r[11] else None,
            "duration": r[12],
        }
        for r in rows
    ]

    errors = client.insert_rows_json(table_id, payload)

    if errors:
        raise Exception(errors)