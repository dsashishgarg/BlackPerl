#Create a ubuntu base image with python 3 installed.
FROM python:3

LABEL maintainer="Ashish Garg <ashishgarg@live.in>"

#Set the working directory
WORKDIR /app

#copy all the files
ADD . /app

#Install the dependencies
RUN apt-get -y update
RUN pip3 install --no-cache-dir -r requirements.txt

#Expose the required port
EXPOSE 5000

#Run the command
ENTRYPOINT ["python"]
CMD ["main.py"]