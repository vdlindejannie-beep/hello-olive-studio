from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'hello_olive_secret_key_change_me'

# Multilingual content dictionary for English and Dutch
TRANSLATIONS = {
    'en': {
        'home': 'Home',
        'shop': 'Shop',
        'contact': 'Custom Request',
        'hero_title': 'Artistry Crafted with',
        'hero_span': 'Precision',
        'hero_sub': 'Fine Art Prints • Custom Apparel • Event Decor • Bespoke Goods',
        'explore': 'Explore Collection',
        'services_title': 'What We Provide',
        's1_title': 'Fine Art Printing',
        's1_desc': 'Museum-grade printing capabilities transforming digital illustrations and photography into breathtaking tactile canvases and prints.',
        's2_title': 'Cricut & Custom Apparel',
        's2_desc': 'Elevated everyday wear, canvas totes, and items meticulously designed and detailed with precision-cut custom elements.',
        's3_title': 'Bespoke Glassware',
        's3_desc': 'Sophisticated glassware items featuring custom monograms and minimalist etchings tailored for high-end gifting and home curation.',
        's4_title': 'Event Decor',
        's4_desc': 'Luxurious signage, welcome displays, and personalized touches designed to make weddings and upscale events unforgettable.',
        'story_title': 'The Hello Olive Aesthetic',
        'story_desc': 'Every piece that leaves our studio is born from a passion for clean lines, high-end design, and exceptional craftsmanship. Whether you are looking for ready-made stock or a personalized statement piece created precisely to your vision, Hello Olive Design Studio brings your aesthetic dreams to reality.',
        'shop_title': 'Curated Stock Collection',
        'shop_sub': 'Hand-crafted goods ready to ship from our studio',
        'inquire': 'Inquire / Order',
        'contact_title': 'Bespoke Inquiries',
        'contact_sub': 'Let’s bring your custom design or event vision to life',
        'name_label': 'Your Name',
        'email_label': 'Email Address',
        'type_label': 'Project / Request Type',
        'message_label': 'Project Details & Vision',
        'submit_btn': 'Submit Request',
        'footer_text': 'Curated Artistry & Custom Goods.'
    },
    'nl': {
        'home': 'Home',
        'shop': 'Winkel',
        'contact': 'Maatwerk Aanvraag',
        'hero_title': 'Vakmanschap Gemaakt met',
        'hero_span': 'Precisie',
        'hero_sub': 'Fine Art Prints • Aangepaste Kleding • Evenement Decor • Unieke Items',
        'explore': 'Bekijk Collectie',
        'services_title': 'Wat Wij Bieden',
        's1_title': 'Fine Art Printing',
        's1_desc': 'Museumwaardige printmogelijkheden die digitale illustraties en fotografie omzetten in adembenemende doeken en prints.',
        's2_title': 'Cricut & Kleding',
        's2_desc': 'Verfijnde alledaagse kleding, canvas tassen en items zorgvuldig ontworpen met precisie-gesneden elementen.',
        's3_title': 'Exclusief Glaswerk',
        's3_desc': 'Verfijnde glaswerkitems met persoonlijke monogrammen en minimalistische etsen voor high-end cadeaus.',
        's4_title': 'Evenement Decor',
        's4_desc': 'Luxe bewegwijzering en gepersonaliseerde details om bruiloften en chique evenementen onvergetelijk te maken.',
        'story_title': 'De Hello Olive Esthetiek',
        'story_desc': 'Elk stuk dat ons atelier verlaat, komt voort uit een passie voor strakke lijnen, high-end design en uitzonderlijk vakmanschap. Of u nu op zoek bent naar kant-en-klare voorraad of een gepersonaliseerd pronkstuk, Hello Olive Design Studio brengt uw dromen tot leven.',
        'shop_title': 'Geselecteerde Voorraad',
        'shop_sub': 'Handgemaakte artikelen direct klaar vanuit ons atelier',
        'inquire': 'Aanvragen / Bestellen',
        'contact_title': 'Maatwerk Verzoeken',
        'contact_sub': 'Laat ons uw aangepaste ontwerp of evenementvisie tot leven brengen',
        'name_label': 'Uw Naam',
        'email_label': 'E-mailadres',
        'type_label': 'Type Project / Verzoek',
        'message_label': 'Projectdetails & Visie',
        'submit_btn': 'Verzoek Verzenden',
        'footer_text': 'Geselecteerde Kunst & Maatwerk.'
    }
}

# Updated product catalog (Hats removed, Fine Art image replaced with a working, verified link)
PRODUCTS = [
    {
        "id": 1,
        "name": "Hand-Pressed Botanical Canvas Tote",
        "price": "$28.00",
        "category": "Accessories",
        "image": "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2,
        "name": "Gilded Custom Glassware Set (Set of 4)",
        "price": "$52.00",
        "category": "Home & Decor",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 3,
        "name": "Limited Edition Fine Art Giclée Print",
        "price": "$75.00",
        "category": "Art Prints",
        "image": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 4,
        "name": "Bespoke Event Welcome Sign & Decor",
        "price": "$120.00",
        "category": "Events",
        "image": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 5,
        "name": "Custom Minimalist Cotton T-Shirt",
        "price": "$32.00",
        "category": "Apparel",
        "image": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=600&q=80"
    }
]

@app.route('/set-lang/<lang>')
def set_lang(lang):
    if lang in ['en', 'nl']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('home'))

def get_t():
    lang = session.get('lang', 'en')
    return TRANSLATIONS[lang], lang

@app.route('/')
def home():
    t, lang = get_t()
    return render_template('index.html', t=t, lang=lang)

@app.route('/shop')
def shop():
    t, lang = get_t()
    return render_template('shop.html', products=PRODUCTS, t=t, lang=lang)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    t, lang = get_t()
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f"Thank you, {name}! Your design inquiry has been received.", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', t=t, lang=lang)

if __name__ == '__main__':
    app.run(debug=True)