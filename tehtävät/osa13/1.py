from flask import Flask, jsonify

app = Flask(__name__)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/prime/<int:n>')
def check_prime(n):
    result = {"Number": n, "isPrime": is_prime(n)}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
