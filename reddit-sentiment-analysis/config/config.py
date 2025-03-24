import configparser
import os

def load_config(config_file='config/config.ini'):
    """
    Loads the config file using configparser and returns the config object.
    Raises FileNotFoundError if the config file is missing.
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found. "
                                "Please create it with your Reddit and PostgreSQL credentials.")
    
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def get_reddit_credentials(config):
    """
    Extracts Reddit credentials from the config object.
    Returns a dictionary with client_id, client_secret, user_agent, username, password.
    """
    reddit_config = config['reddit']
    return {
        'client_id': reddit_config.get('client_id'),
        'client_secret': reddit_config.get('client_secret'),
        'user_agent': reddit_config.get('user_agent'),
        'username': reddit_config.get('username'),
        'password': reddit_config.get('password')
    }

def get_postgres_credentials(config):
    """
    Extracts PostgreSQL credentials from the config object.
    Returns a dictionary with db_user, db_password, db_host, db_port, db_name.
    """
    postgres_config = config['postgresql']
    return {
        'db_user': postgres_config.get('db_user'),
        'db_password': postgres_config.get('db_password'),
        'db_host': postgres_config.get('db_host'),
        'db_port': postgres_config.get('db_port'),
        'db_name': postgres_config.get('db_name')
    }

if __name__ == "__main__":
    # Example usage
    try:
        cfg = load_config()  # Load config from the default path
        reddit_creds = get_reddit_credentials(cfg)
        pg_creds = get_postgres_credentials(cfg)

        print("Reddit Credentials:", reddit_creds)
        print("PostgreSQL Credentials:", pg_creds)
    except FileNotFoundError as e:
        print(e)
