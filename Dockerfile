FROM python:3.7
WORKDIR /web-song-share

COPY requirements.txt /web-song-share
RUN apt-get update && apt-get install sudo
# RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0 \
#     python3-pip \
#     cmake \ 
#     musl-dev \
#     openssh-client \
#     git \
#     default-libmysqlclient-dev\
#     g++ \
#     libffi-dev \
#     make \
#     ffmpeg \
#     vim \
    # && pip3 install --upgrade pip \
    # && rm -f /var/cache/apk/* \
    # && rm -rf ~/.cache \
RUN pip3 install --no-cache-dir --compile -r requirements.txt

COPY ./ /web-song-share/

CMD ["sudo", "gunicorn", "-w", "1", "-b", "0.0.0.0:80", "app:app"]
# CMD ["python3", "app.py"]
# gunicorn -w 1 -b 0.0.0.0:80 run:app --daemon
