#!python

from flask import Flask, request, Response
from neo4j import GraphDatabase
from json import dumps

app = Flask(__name__)

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "neo4j123"))

def serialize_record(return_val):
    return {
        "name": return_val["name"],
    }

@app.route('/')
def query_neo():
    def work(tx,fio):
        return list(tx.run(
            "MATCH(a:Person)-[*]->(b) WHERE b.name = $fio "
            "RETURN a,b",
            {"fio": fio}
        ))
    fio = request.args.get('fio')
    # fio = 'Медведева Дарья Алексеевна'
    records = driver.session().read_transaction(work, fio)
    data = [serialize_record(record["a"]) for record in records]
    out = dumps(data,sort_keys=False,indent=4,ensure_ascii=False,separators=(',', ': '))
    return Response(fio+' <- '+out,mimetype="application/json")

if __name__ == '__main__':
#     #run app in debug mode on port 5000
    app.run(debug=True, port=5000)
