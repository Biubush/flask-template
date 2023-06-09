from app import app, func

if __name__ == "__main__":
    func.check_and_migrate()
    app.run()
