from .database import SessionLocal

def get_session_current_db():
    try:
        session_current = SessionLocal()
        yield session_current
    finally:
        session_current.close()
