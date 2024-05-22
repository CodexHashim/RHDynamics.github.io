from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample product data
products = {
    "EMEE": {"price": 100, "mfg_date": "10/10/2023", "exp_date": "10/10/2026", "inventory": "a1"},
    # Add more products as needed
}

@app.route('/product')
def product():
    name = request.args.get('name')
    product = products.get(name)
    if product:
        return render_template_string('''
            <h1>{{ name }}</h1>
            <p>Price: {{ product['price'] }}</p>
            <p>MFG Date: {{ product['mfg_date'] }}</p>
            <p>EXP Date: {{ product['exp_date'] }}</p>
            <p>Inventory: {{ product['inventory'] }}</p>
        ''', name=name, product=product)
    else:
        return "Product not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
