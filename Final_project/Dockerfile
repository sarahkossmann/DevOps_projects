FROM python:3.9
RUN mkdir "/game"
COPY ./ /game/
WORKDIR /game
RUN python3 -m pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main_score.py"]