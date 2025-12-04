from .operations import config
import json


def get_shop(shop: dict):
    shops = config.cur.execute("""
        SELECT * FROM zakaz order by id
    """)
    # Get column names for dictionary keys (optional)
    column_names = [col[0] for col in config.cur.description]
    # Fetch all rows
    rows = config.cur.fetchall()

    # Convert to a list of dictionaries
    data_as_dicts = []
    for row in rows:
        row_dict = {}
        for i, col_name in enumerate(column_names):
            row_dict[col_name.lower()] = row[
                i
            ]  # Convert column names to lowercase for consistency
        data_as_dicts.append(row_dict)

    for shop in shops:
        print(f"shops: {shop}")
    # Serialize the list of dictionaries to a JSON string
    json_output = json.dumps(data_as_dicts, indent=4)  # indent for pretty printing

    print(json_output)

