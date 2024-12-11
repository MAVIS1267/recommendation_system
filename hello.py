from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return "Hello from recommendation-system!"


if __name__ == "__main__":
    main()
