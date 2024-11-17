from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate
import geopandas as gpd
import pandas as pd
from shapely import to_geojson
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", "8000"))


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

cors = CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class ProvinceItems(db.Model):
    __tablename__ = "province_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    province_id = Column(Integer)
    item_name = Column(String)
    img_url = Column(String)


@app.get("/")
def test_app():
    return <h1>Hello world</h1>


@app.get("/get_province/")
def get_province():
    try:
        province_name = request.args.get("province_name")
        province_name = province_name.lower()

        # read geojson file
        gs = gpd.read_file("./province.geojson")
        # convert geometric series into dataframe
        df = pd.DataFrame(gs)
        result = df[df["PR_NAME"].str.lower() == province_name].loc[
            :, ["PR_NAME", "geometry", "PROVINCE"]
        ]
        geometry = result["geometry"].values[0]
        pr_name = result["PR_NAME"].values[0]
        province_id = int(result["PROVINCE"].values[0])
        sql = db.session.query(ProvinceItems).filter(
            ProvinceItems.province_id == province_id
        )
        results = sql.all()  # Fetch all ORM objects

        items = []
        for item in results:
            del item.__dict__["_sa_instance_state"]
            items.append(item.__dict__)

        geojson_obj = to_geojson(geometry)

        return jsonify(
            {"data": {"pr_name": pr_name, "geojson": geojson_obj, "items": items}}
        )
    except Exception as err:
        return jsonify({"error": str(err)})


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8000, debug=True)
    app.run(port=PORT)
    print(f"listening on port {PORT}")
