import cx_Oracle
import db_config
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cur = con.cursor()

class Employees(Resource):

    def get(self):
        def converToDict(res):
            resList = []
            for item in res:
                resDict = {}
                resDict["id"] = item[0]
                resDict["first name"] = item[1]
                resDict["last name"] = item[2]
                resDict["salary"] = item[3]
                resList.append(resDict.copy())
            return resList

        cur.execute("select Employee_id, First_Name, Last_Name, SALARY from HR.EMPLOYEES where DEPARTMENT_ID =100")
        res = cur.fetchall()
        resList= converToDict(res)
        return {'employees': resList}


api.add_resource(Employees, '/employees') # Route_1

if __name__ == '__main__':
    app.run(port='5002')
