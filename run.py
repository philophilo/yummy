from app import app

app.secret_key = "kj][p]l/=7<F9>j 9877<F10>q2e"
app.config['SESSION_TYPE'] = "filesystem"
app.debug=True

if __name__ == "__main__":
    app.run(port=3030)
