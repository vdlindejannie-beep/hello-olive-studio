from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'hello_olive_secret_key_change_me'

# Mock product data for the shop page showcasing Cricut & print capabilities
PRODUCTS = [
    {
        "id": 1,
        "name": "Custom Embroidered & Vinyl Monogram Hat",
        "price": "$34.00",
        "category": "Apparel",
        "image": "https://images.unsplash.com/photo-1521369909029-2afed882baee?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2,
        "name": "Hand-Pressed Botanical Canvas Tote",
        "price": "$28.00",
        "category": "Accessories",
        "image": "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 3,
        "name": "Gilded Custom Glassware Set (Set of 4)",
        "price": "$52.00",
        "category": "Home & Decor",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 4,
        "name": "Limited Edition Fine Art Giclée Print",
        "price": "$75.00",
        "category": "Art Prints",
        "image": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 5,
        "name": "Bespoke Event Welcome Sign & Decor",
        "price": "$120.00",
        "category": "Events",
        "image": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 6,
        "name": "Custom Minimalist Cotton T-Shirt",
        "price": "$32.00",
        "category": "Apparel",
        "image": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=600&q=80"
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html', products=PRODUCTS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        project_type = request.form.get('project_type')
        message = request.form.get('message')
        
        # In a live app, you would send an email or save to a database here.
        flash(f"Thank you, {name}! Your design inquiry has been received. We will contact you shortly.", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)