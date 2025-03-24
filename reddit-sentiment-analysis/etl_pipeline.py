import subprocess
import logging

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)

def run_extraction():
    logger.info("Starting Reddit extraction...")
    subprocess.run(["python", "etl/reddit_extraction.py"], check=True)
    logger.info("Reddit extraction completed.\n")

def run_sentiment():
    logger.info("Starting sentiment analysis...")
    subprocess.run(["python", "analysis/sentiment_analysis.py"], check=True)
    logger.info("Sentiment analysis completed.\n")

def run_ingestion():
    logger.info("Starting conditional ingestion...")
    subprocess.run(["python", "db/conditional_ingest.py"], check=True)
    logger.info("Conditional ingestion completed.\n")

def main():
    logger.info("Pipeline execution started.\n")
    try:
        run_extraction()
        logger.info("Extraction stage finished. Proceeding to sentiment analysis...\n")

        run_sentiment()
        logger.info("Sentiment analysis stage finished. Proceeding to data ingestion...\n")

        run_ingestion()
        logger.info("Pipeline completed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"An error occurred during pipeline execution: {e}", exc_info=True)

if __name__ == "__main__":
    main()
