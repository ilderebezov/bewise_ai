from __future__ import annotations
from sqlalchemy import Column, BigInteger, Integer, DateTime, UnicodeText
from src.models.base_model import BaseModel
import sql
import datetime


class Question_tb(BaseModel):
    __tablename__ = "question"

    Id = Column(BigInteger, primary_key=True, autoincrement=True)

    IdExternal = Column(BigInteger, unique=True)
    Body = Column(UnicodeText())
    Answer = Column(UnicodeText())
    CreationDate = Column(DateTime)

    @staticmethod
    def get_or_create(id_external: int = None,
                      body: str = None,
                      answer: str = None,
                      creation_date: datetime = None,
                      ) -> Question_tb:
        """

        :param id_external:
        :param body:
        :param answer:
        :param creation_date:
        :return:
        """

        instance = sql.session.query(Question_tb).filter(Question_tb.IdExternal == id_external).first()

        if instance is None:
            instance = Question_tb(
                IdExternal=id_external,
                Body=body,
                Answer=answer,
                CreationDate=creation_date,
                )
            sql.session.add(instance)
            sql.protected_commit()
