import sql
from src.models.base_model import BaseModel
from src.models.question import Question_tb

BaseModel.metadata.create_all(sql.engine)
