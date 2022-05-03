from datetime import datetime

import requests
from loguru import logger

import sql
from src.models.question import Question_tb


class Question:
    def __init__(self, id, question, answer, created_at):
        self.id = id
        self.question = question
        self.answer = answer
        self.created_at = created_at


def get_question():
    link = f"https://jservice.io/api/random?count=1"
    req_question = requests.get(link)
    req_question = req_question.json()

    creation_date = req_question[0]['created_at']
    creation_date = datetime.fromisoformat(creation_date[:-1] + '+00:00')
    question = Question(req_question[0]['id'],
                        req_question[0]['question'],
                        req_question[0]['answer'],
                        creation_date
                        )
    return question


def question_check(question: Question):
    return sql.session.query(Question_tb.Id).filter(Question_tb.IdExternal == question.id).first()


def get_questions(questions_number: int):

    for question in range(questions_number):

        question = get_question()
        question_in_base = True
        number = 0
        while question_in_base is True:
            number += 1
            check_question = question_check(question)
            if check_question is None:
                Question_tb.get_or_create(id_external=question.id,
                                          body=question.question,
                                          answer=question.answer,
                                          creation_date=question.created_at,
                                          )
                question_in_base = False
                logger.info(f'Question id : {question.id} was added to base.')

            if number == 100:
                Question_tb.get_or_create()
                logger.info(f'Empty question was added to base.')
                break
