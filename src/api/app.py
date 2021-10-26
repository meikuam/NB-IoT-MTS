from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import logging
import sys
sys.path.append("..")
from src.bd.base import fetch_data
from src.bd.engine.postgres import engine

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    last_n_rows = 15
    table_name = "telemetry"
    index_col = "date"
    data_df = pd.DataFrame()
    try:
        # TODO: add smth like that to fetch_data:
        # query=f"SELECT * FROM {table_name} order by {index_col} desc limit {last_n_rows};"
        data_df = fetch_data(table_name, engine).sort_values("date", ascending=False).head(last_n_rows)
    except Exception as e:
        logging.error(f"fastapi.read_root: {e}")
    html_string = f"""
        <html>
        <head>
        <title>NB-IoT</title>
        <script> 
        setTimeout(function(){{
            window.location.reload(1);
        }}, 5000);
        </script>
        </head>
        <body>
        <h1>Последние {last_n_rows} измерений</h1>
        {data_df.to_html()}
        </body>
        </html>
    """
    return html_string