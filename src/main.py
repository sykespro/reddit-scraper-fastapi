import fastapi as _fastapi
import fastapi.responses as _responses

app = _fastapi.FastAPI(
    title="Reddit + Scraper + FastAPI",
    description="The purpose of this project is to test FastAPI and Scraping Reddit.",
    version="0.0.1"
)

import services as _services


@app.get("/")
def root():
    return {"message": "welcome to the amazing meme api"}


@app.get("/general-memes")
def get_general_memes():
    image_path = _services.select_random_image("memes")
    return _responses.FileResponse(image_path)


@app.post("/general-memes")
def create_general_meme(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_image("memes", image)
    if file_path is None:
        return _fastapi.HTTPException(status_code=409, detail="incorrect file type")
    return _responses.FileResponse(file_path)
