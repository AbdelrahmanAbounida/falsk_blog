from app import create_app

app = create_app()

print(app.config['MONGO_URI'])

if __name__ == "__main__":
    app.run(debug=True)