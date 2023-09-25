import redis

# Replace with your DigitalOcean Redis connection details
username = "default"
password = "AVNS_VePqOdgNdEIZ1QLFgKY"
host = "rediss://chathistoryredis-do-user-14562213-0.b.db.ondigitalocean.com"
port = 25061

try:
    r = redis.StrictRedis(
        host=host,
        port=port,
        password=password,
        decode_responses=True,  # Convert byte responses to strings
    )
    r.ping()  # Test the connection
    print("Connected to Redis!")
except Exception as e:
    print(f"Failed to connect to Redis: {e}")
