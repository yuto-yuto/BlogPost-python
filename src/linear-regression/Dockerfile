FROM yutona/python-dev

RUN pip install numpy==1.20.1
RUN pip install matplotlib==3.3.4
RUN pip install seaborn==0.11.1
RUN mkdir -p /src/images

WORKDIR /src
COPY ./dataset/housing.csv /src/dataset/
# CMD [ "python", "process.py" ]
CMD [ "sh" ]

COPY ./*.py ./
