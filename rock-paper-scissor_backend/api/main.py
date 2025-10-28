# api/main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from rock_paper_scissor.model import get_model, predict_image

from tests.logging_config import configure_logging
import logging
from PIL import Image
import io

######################################
###  get_model() → loads and caches your EfficientNet model at startup
###  predict_image() → runs inference on a PIL image and returns the result dictionary
######################################

app = FastAPI() # title="RPS API"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_BYTES = 5 * 1024 * 1024  # 5MB

@app.on_event("startup")
def startup_event():
    # Load model once
    get_model()

@app.get("/")
def root():
    return {"message": "Rock Paper Scissor API is running!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type or "image" not in file.content_type:
        raise HTTPException(status_code=400, detail="Please upload an image file (jpg/png).")

    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="Empty file.")
    if len(data) > MAX_BYTES:
        raise HTTPException(status_code=413, detail="File too large.")

    try:
        pil_img = Image.open(io.BytesIO(data))
        result = predict_image(pil_img)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {e}")

configure_logging()
logger = logging.getLogger("api")


#app = FastAPI()
# ... middleware config ...

@app.on_event("startup")
def startup_event():
    logger.info("Starting RPS API - loading model")
    try:
        get_model()  # load and cache
        logger.info("Model loaded successfully.")
    except Exception as e:
        logger.exception("Failed to load model at startup: %s", e)
        # decide whether to raise or continue - raising stops server
        raise
