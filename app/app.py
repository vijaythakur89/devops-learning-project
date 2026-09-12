import sqlite3
import time
import pandas as pd
import streamlit as st

# --- DATABASE SETUP ---
DB_NAME = "blinkit_demo.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            unit TEXT NOT NULL,
            image_url TEXT
        )
    """
    )

    c.execute("SELECT COUNT(*) FROM products")
    if c.fetchone()[0] == 0:
        sample_products = [
            (
                "Amul Taaza Toned Milk",
                "Dairy & Bread",
                27.0,
                50,
                "500 ml",
                "https://images.unsplash.com/photo-1563636619-e9143da7973b?w=300",
            ),
            (
                "Harvest Gold White Bread",
                "Dairy & Bread",
                40.0,
                30,
                "400 g",
                "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=300",
            ),
            (
                "Fresh Bananas",
                "Fruits & Vegetables",
                35.0,
                40,
                "1 kg",
                "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=300",
            ),
            (
                "Hybrid Tomatoes",
                "Fruits & Vegetables",
                22.0,
                60,
                "500 g",
                "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?w=300",
            ),
            (
                "Lay's India's Magic Masala",
                "Munchies",
                20.0,
                100,
                "50 g",
                "https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=300",
            ),
            (
                "Coca-Cola Original Taste",
                "Cold Drinks & Juices",
                40.0,
                45,
                "750 ml",
                "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=300",
            ),
            (
                "Maggi 2-Minute Noodles",
                "Instant Food",
                14.0,
                80,
                "70 g",
                "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?w=300",
            ),
            (
                "Fortune Sunlite Sunflower Oil",
                "Atta, Rice & Oil",
                145.0,
                25,
                "1 L",
                "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=300",
            ),
        ]
        c.executemany(
            """
            INSERT INTO products (name, category, price, stock, unit, image_url)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            sample_products,
        )

    conn.commit()
    conn.close()


def get_products():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM products", conn)
    conn.close()
    return df


def update_stock(cart):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for item_id, item in cart.items():
        c.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (item["qty"], item_id),
        )
    conn.commit()
    conn.close()


# --- STREAMLIT CONFIG & SCOPED CUSTOM CSS ---
st.set_page_config(page_title="Blinkit Local Demo", page_icon="⚡", layout="wide")

st.markdown(
    """
    <style>
    /* Fixed image height with crop */
    div[data-testid="stImage"] img {
        height: 160px !important;
        object-fit: cover !important;
        border-radius: 12px !important;
    }
    
    /* Target only product cards using a dedicated wrapper class */
    .product-card {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 380px;
        padding: 12px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #ffffff;
        margin-bottom: 20px;
    }

    .product-card button {
        margin-top: auto !important;
        width: 100%;
    }
    </style>
""",
    unsafe_allow_html=True,
)

init_db()

# Initialize Session State
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "order_status" not in st.session_state:
    st.session_state.order_status = None

# --- HEADER SECTION ---
st.title("⚡ Blinkit Local Express")
st.caption("Delivery in **10 minutes** to your doorstep")
st.divider()

# --- SIDEBAR: CART MANAGEMENT ---
st.sidebar.header("🛒 Your Cart")

if not st.session_state.cart:
    st.sidebar.info("Your cart is empty.")
else:
    total_amount = 0
    items_to_remove = []

    for item_id, item in st.session_state.cart.items():
        item_total = item["price"] * item["qty"]
        total_amount += item_total

        col1, col2, col3 = st.sidebar.columns([3, 1, 1])
        col1.write(f"**{item['name']}**\n₹{item['price']} x {item['qty']}")

        if col2.button("➕", key=f"add_{item_id}"):
            if item["qty"] < item["stock"]:
                st.session_state.cart[item_id]["qty"] += 1
                st.rerun()
            else:
                st.sidebar.warning("Stock limit reached")

        if col3.button("➖", key=f"sub_{item_id}"):
            st.session_state.cart[item_id]["qty"] -= 1
            if st.session_state.cart[item_id]["qty"] <= 0:
                items_to_remove.append(item_id)
            st.rerun()

    for item_id in items_to_remove:
        del st.session_state.cart[item_id]

    st.sidebar.divider()
    delivery_fee = 15.0 if total_amount < 200 else 0.0
    grand_total = total_amount + delivery_fee

    st.sidebar.write(f"**Items Total:** ₹{total_amount:.2f}")
    st.sidebar.write(f"**Delivery Fee:** ₹{delivery_fee:.2f}")
    st.sidebar.subheader(f"Grand Total: ₹{grand_total:.2f}")

    # Checkout Form
    address = st.sidebar.text_input(
        "Delivery Address", "House 12, Block B, Local Street"
    )
    if st.sidebar.button("📦 Place 10-Min Delivery Order", type="primary"):
        if not address.strip():
            st.sidebar.error("Please enter a valid address.")
        else:
            update_stock(st.session_state.cart)
            st.session_state.order_status = {
                "address": address,
                "total": grand_total,
                "items": st.session_state.cart.copy(),
            }
            st.session_state.cart = {}
            st.rerun()

# --- MAIN CONTENT: PRODUCT CATALOG ---
df_products = get_products()

# Search & Filter Controls (Clean inputs without card wrapper)
col_search, col_cat = st.columns([3, 2])
search_query = col_search.text_input("🔍 Search for products, brands, or items...")
categories = ["All"] + list(df_products["category"].unique())
selected_category = col_cat.selectbox("Category", categories)

# Apply Filters
filtered_df = df_products.copy()
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]
if search_query:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(search_query, case=False)
    ]

# Order Tracking Overlay
if st.session_state.order_status:
    st.success("🎉 Order Placed Successfully!")
    st.info(f"**Delivering to:** {st.session_state.order_status['address']}")

    progress_bar = st.progress(0)
    status_text = st.empty()

    statuses = [
        ("Packing your items at nearest dark store...", 25),
        ("Rider assigned! On the way to pickup...", 50),
        ("Out for delivery (Rider 1.2 km away)...", 75),
        ("Arrived at location! Enjoy your products 🎉", 100),
    ]

    for status, pct in statuses:
        status_text.markdown(f"**Status:** {status}")
        progress_bar.progress(pct)
        time.sleep(1.2)

    if st.button("Dismiss Order Tracker"):
        st.session_state.order_status = None
        st.rerun()
    st.divider()

# Product Grid Display
st.subheader("Explore Products")

# Render 4 columns per row wrapped inside styled cards
for i in range(0, len(filtered_df), 4):
    cols = st.columns(4)
    batch = filtered_df.iloc[i : i + 4]

    for idx, (_, row) in enumerate(batch.iterrows()):
        with cols[idx]:
            # Container for Scoped Product Card Styling
            with st.container():
                st.image(row["image_url"], use_container_width=True)
                st.markdown(f"**{row['name']}**")
                st.caption(f"{row['unit']} | Stock: {row['stock']}")
                st.markdown(f"### ₹{row['price']}")

                if row["stock"] <= 0:
                    st.error("Out of Stock")
                else:
                    if st.button("Add to Cart", key=f"add_catalog_{row['id']}"):
                        item_id = int(row["id"])
                        if item_id in st.session_state.cart:
                            if st.session_state.cart[item_id]["qty"] < row["stock"]:
                                st.session_state.cart[item_id]["qty"] += 1
                        else:
                            st.session_state.cart[item_id] = {
                                "name": row["name"],
                                "price": row["price"],
                                "qty": 1,
                                "stock": row["stock"],
                            }
                        st.rerun()
