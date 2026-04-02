# myfastapiapp/scripts/run.py
import uvicorn
from myfastapiapp import app  # Import your FastAPI app instance


def run_server():
    """Start the Uvicorn server with specified settings."""
    uvicorn.run(
        app="myfastapiapp:app",  # Path to your app instance
        host="0.0.0.0",  # Listen on all network interfaces
        port=8000,  # Port to use
        reload=True,  # Enable auto-reload (development)
        # workers=4,            # Uncomment to use multiple workers (production)
        # Note: `reload` and `workers` cannot be used together!
    )


if __name__ == "__main__":
    run_server()