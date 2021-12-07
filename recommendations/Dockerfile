FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs
COPY recommendations/ /service/recommendations
WORKDIR /service/recommendations
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 50051
ENTRYPOINT ["python3", "recommendations.py"]
