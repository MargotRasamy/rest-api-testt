FROM python:3.10-alpine

RUN pip install fastapi
RUN pip install pymongo
RUN pip install pydantic
RUN pip install uvicorn

COPY . .

EXPOSE 3500

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3500" ]