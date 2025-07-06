import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="postgresql",
    connection_options={
        "url": "jdbc:postgresql://your-db-host/dbname",
        "user": "username",
        "password": "password",
        "dbtable": "public.users"
    }
)

output_path = "s3://your-output-bucket/csv/"
glueContext.write_dynamic_frame.from_options(
    frame=dyf,
    connection_type="s3",
    format="csv",
    connection_options={"path": output_path}
)

job.commit()
