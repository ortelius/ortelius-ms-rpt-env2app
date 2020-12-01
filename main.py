import os

import psycopg2
from flask import Flask
from flask_restful import Api, Resource

# Init Flask
app = Flask(__name__)
api = Api(app)

# Init db connection
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "postgres")
db_user = os.getenv("DB_USER", "postgres")
db_pass = os.getenv("DB_PASS", "postgres")

conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)

# Env2APPList
# shows a list of all environments that an application has been deployed to


class Env2AppList(Resource):
    def get(self):
        cursor = conn.cursor()
        sql = "select a.id, a.name, b.id, b.name, c.deploymentid from dm.dm_environment a, dm.dm_application b, dm.dm_deployment c where a.id = c.envid and b.id = c.appid order by 2, 4, 5"
        result = []
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            cols = {}
            cols['envid'] = row[0]
            cols['envname'] = row[1]
            cols['appid'] = row[2]
            cols['appname'] = row[3]
            cols['deploymentid'] = row[4]
            result.append(cols)
            row = cursor.fetchone()

        return result


##
# Actually setup the Api resource routing here
##
api.add_resource(Env2AppList, '/msapi/env2app')

if __name__ == '__main__':
    if (os.getenv('FLASK_ENV', "") == "development"):
        app.run(host="0.0.0.0", port=5000)
    else:
        serve(app, host='0.0.0.0', port=5000)
