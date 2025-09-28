from flask import Flask, render_template, request

app = Flask(__name__)

cakes = [
    {"name": "玫瑰烤焦了", "price": 15, "img": "static/strawberry.jpg"},
    {"name": "斑斓", "price": 18, "img": "static/chocolate.jpg"},
    {"name": "云顶海盐椰蓝", "price": 20, "img": "static/matcha.jpg"}
]

@app.route("/")
def home():
    return render_template("index.html", cakes=cakes)

@app.route("/order", methods=["POST"])
def order():
    name = request.form["name"]
    phone = request.form["phone"]
    cake = request.form["cake"]
    qty = request.form["qty"]
    print(f"新订单：{name}, {phone}, {cake}, 数量 {qty}")
    return f"订单提交成功！谢谢 {name}，我们会尽快联系你。"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
