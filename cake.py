{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8e2c5c7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [28/Sep/2025 01:00:49] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Sep/2025 01:00:49] \"GET /static/chocolate.jpg HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Sep/2025 01:00:49] \"GET /static/matcha.jpg HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Sep/2025 01:00:49] \"GET /static/strawberry.jpg HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Sep/2025 01:00:57] \"POST /order HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "新订单：, , 草莓小蛋糕, 数量 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [28/Sep/2025 01:01:22] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Sep/2025 01:01:22] \"GET /static/strawberry.jpg HTTP/1.1\" 304 -\n",
      "127.0.0.1 - - [28/Sep/2025 01:01:22] \"GET /static/matcha.jpg HTTP/1.1\" 304 -\n",
      "127.0.0.1 - - [28/Sep/2025 01:01:22] \"GET /static/chocolate.jpg HTTP/1.1\" 304 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# 模拟小蛋糕菜单\n",
    "cakes = [\n",
    "    {\"name\": \"草莓小蛋糕\", \"price\": 15, \"img\": \"static/strawberry.jpg\"},\n",
    "    {\"name\": \"巧克力小蛋糕\", \"price\": 18, \"img\": \"static/chocolate.jpg\"},\n",
    "    {\"name\": \"抹茶小蛋糕\", \"price\": 20, \"img\": \"static/matcha.jpg\"}\n",
    "]\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template(\"index.html\", cakes=cakes)\n",
    "\n",
    "@app.route(\"/order\", methods=[\"POST\"])\n",
    "def order():\n",
    "    name = request.form[\"name\"]\n",
    "    phone = request.form[\"phone\"]\n",
    "    cake = request.form[\"cake\"]\n",
    "    qty = request.form[\"qty\"]\n",
    "\n",
    "    # 这里先简单打印（实际可以存数据库或发邮件通知你）\n",
    "    print(f\"新订单：{name}, {phone}, {cake}, 数量 {qty}\")\n",
    "\n",
    "    return f\"订单提交成功！谢谢 {name}，我们会尽快联系你。\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=False, use_reloader=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ab083ed",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c67cf169",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eebb631e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "760db0b2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "e66bb3c2",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
