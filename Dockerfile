# Use a base Python image
FROM nikolaik/python-nodejs:python3.9-nodejs16

# Set environment variables
ENV WORKDIR=/home/src/app

# Create WORKDIR
RUN mkdir -p $WORKDIR

# Copy necessary folders into the container
COPY web2py/ $WORKDIR/web2py/
COPY requirements.txt $WORKDIR

# Build node dependencies
WORKDIR $WORKDIR/web2py/applications/school/
RUN npm install
RUN npm run build

# Build Python dependencies
WORKDIR $WORKDIR
RUN pip install -r requirements.txt

# Expose the port on which web2py runs
EXPOSE 8000

# Entry point to run web2py with the specified password
CMD ["python", "web2py/web2py.py", "-a", "${ADMIN_PASSWORD}", "-i", "0.0.0.0", "-p", "8000"]