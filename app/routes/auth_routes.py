from fastapi import APIRouter, HTTPException
from app.database import get_db_connection
from app.models.auth_models import RegisterUser, LoginUser

auth_router = APIRouter()

@auth_router.post("/register")
def register_user(user: RegisterUser):
    conn = get_db_connection()
    cur = conn.cursor()

    import random, string
    u_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    try:
        cur.execute("CALL register_user(%s, %s, %s);", (u_id, user.email, user.password))
        conn.commit()
        return {"message": "User registered successfully", "u_id": u_id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")
    finally:
        cur.close()
        conn.close()

@auth_router.post("/login")
def login_user(user: LoginUser):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT authenticate_user(%s, %s);", (user.email, user.password))
        uid = cur.fetchone()[0]

        if uid:
            return {"message": "Login successful", "u_id": uid}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")
    finally:
        cur.close()
        conn.close()
