# Using Python Slim-Buster
FROM biansepang/weebproject:buster

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/kirito-1240/TempestUB /home/TEMPEST-USERBOT/ \
    && chmod 777 /home/TEMPEST-USERBOT \
    && mkdir /home/TEMPEST-USERBOT/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/TEMPEST-USERBOT/

# Setup Working Directory
WORKDIR /home/TEMPEST-USERBOT/

# Finalization
CMD ["python3","-m","userbot"]
