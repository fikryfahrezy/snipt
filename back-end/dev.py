import uvicorn

if __name__ == "__main__":
    uvicorn.run("snipt:app", port=5050, log_level="info", reload=True)
