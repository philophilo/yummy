from app import app


if __name__ == "__main__":
    app.secret_key = "kj][p]l/=7<F9>j 9877<F10>q2e"
    app.config['SESSION_TYPE'] = "filesystem"
    app.run(port=3030, debug=True)
