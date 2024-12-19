# Use the official OpenJDK image that includes Java 11
FROM openjdk:11-jdk-slim

# Set environment variables for Python and PySpark
ENV PYTHON_VERSION=3.8
ENV SPARK_VERSION=3.1.2
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Install Python, wget, and tar
RUN apt-get update && apt-get install -y python3 python3-pip wget tar && apt-get clean

# Download and install Apache Spark
RUN wget -qO- https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz | tar xvz -C /opt \
    && ln -s /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY app.py /app/app.py

WORKDIR /app

# Command to run the application (adjust as needed)
CMD ["python3", "app.py"]