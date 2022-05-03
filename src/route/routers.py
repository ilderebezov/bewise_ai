
from flask import Flask, request
from loguru import logger

from src.request.question_request import get_questions

app = Flask(__name__)


@app.route('/to_db', methods=['POST'])
def question_to_db():
    # curl -H "Content-Type: application/json" -X POST -d '{"questions_num": 1}' http://127.0.0.1:5000/to_db
    response = request.get_json()
    logger.info(f'Request in: {response}')
    get_questions(response['questions_num'])
    return 'Ok', 200
