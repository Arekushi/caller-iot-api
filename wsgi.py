from src.app import create_app

app = create_app()

if __name__ == '__main__':
    if app.config.FLASK_ENV == 'development':
        app.run(
            host=app.config.HOST,
            port=app.config.PORT
        )
    else:
        app.run()
