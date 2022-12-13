FROM python:3.9
COPY main_score.py /main_score.py
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
CMD ["python", "main_score.py"]