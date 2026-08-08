import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# 1. PAGE SETUP & MASTER LUXURY PURPLE THEME

st.set_page_config(
    page_title="Executive Operations Control Room", layout="wide")

# Custom UI Overhaul: Lighter Deep Purple Canvas + Graphite Black Component Slots
st.markdown("""
    <style>
    /* Premium Deep Purple Canvas - Brightened by 20% from baseline dark */
    .stApp {
        background-color: #221B33 !important;
        color: #E2E8F0 !important;
    }
    
    /* Graphite Black Sidebar Control Panel */
    section[data-testid="stSidebar"] {
        background-color: #16181D !important;
        border-right: 2px solid #362B52 !important;
    }
    
    /* Global typography clarity rules */
    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #FFFFFF !important;
    }
    
    /* High Visibility Rules for Control Filter Elements */
    div[data-testid="stWidgetLabel"] p {
        font-size: 14px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px;
        color: #FFFFFF !important;
    }
    
    .stMultiSelect div[data-baseweb="select"] {
        background-color: #1A1C23 !important;
        border: 1px solid #52427A !important;
    }
    
    span[data-baseweb="tag"] {
        background-color: #58A6FF !important; 
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    
    /* Keep drop-down menu items visible and white on hover selections */
    div[data-baseweb="popover"] li, div[data-baseweb="select"] div {
        color: #FFFFFF !important;
    }

    /* Light Black Background Component KPI Containers */
    .metric-card {
        background-color: #1A1C23;
        border: 1px solid #362B52;
        border-radius: 8px;
        padding: 16px 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .metric-card:hover {
        border-color: #58A6FF;
        transform: translateY(-2px);
    }
    .metric-label {
        font-size: 11px;
        color: #A0AEC0;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 6px;
    }
    .metric-val {
        font-size: 24px;
        font-weight: 700;
        color: #58A6FF;
    }
    
    /* Light Black Background behind each graph slot */
    .chart-slot {
        background-color: #1A1C23;
        border: 1px solid #362B52;
        border-radius: 8px;
        padding: 18px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)


# 2. DATA PROCESSING PIPELINE

@st.cache_data
def load_data():
    df = pd.read_csv("Clean_Online_Store_Orders.csv")
    df = df.rename(columns={'Date': 'order_date'})
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    return df


df = load_data()


# 3. INTERACTIVE SIDEBAR CONTROL PANEL

st.sidebar.title(" Dashboard Filters")
st.sidebar.markdown("Adjust selections below to modify all metrics live.")
st.sidebar.write("---")

available_years = sorted(df['year'].dropna().unique().tolist())
selected_years = st.sidebar.multiselect(
    "Operating Year:", available_years, default=available_years)

available_status = sorted(df['OrderStatus'].dropna().unique().tolist())
selected_status = st.sidebar.multiselect(
    "Fulfillment Status:", available_status, default=available_status)

# Mutate active dataframe layer
filtered_df = df[
    (df['year'].isin(selected_years)) &
    (df['OrderStatus'].isin(selected_status))
]


# 4. DASHBOARD HEADER HERO

st.title("Enterprise Store Performance Analytics")
st.markdown("##### A comprehensive executive analysis of catalog inventory performance and operational transaction trends.")
st.write("")


# 5. HIGH-DENSITY METRICS ROW

total_revenue = filtered_df['TotalPrice'].sum()
total_orders = filtered_df['OrderID'].nunique()
aov = filtered_df['TotalPrice'].mean() if total_orders > 0 else 0

top_payment = filtered_df['PaymentMethod'].mode(
)[0] if not filtered_df['PaymentMethod'].empty else "N/A"
top_referral = filtered_df['ReferralSource'].mode(
)[0] if not filtered_df['ReferralSource'].empty else "N/A"

m_col1, m_col2, m_col3, m_col4, m_col5 = st.columns(5)

with m_col1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Total Revenue</div><div class="metric-val">${total_revenue:,.2f}</div></div>', unsafe_allow_html=True)
with m_col2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Total Orders</div><div class="metric-val">{total_orders:,}</div></div>', unsafe_allow_html=True)
with m_col3:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Average Order Value</div><div class="metric-val">${aov:,.2f}</div></div>', unsafe_allow_html=True)
with m_col4:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Top Payment Channel</div><div class="metric-val" style="font-size:16px; padding-top:6px; color:#34D399; font-weight:bold;">{top_payment}</div></div>', unsafe_allow_html=True)
with m_col5:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Top Referral Source</div><div class="metric-val" style="font-size:16px; padding-top:6px; color:#FBBF24; font-weight:bold;">{top_referral}</div></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# 6. ROW 1: 3-COLUMN ANALYTICAL GRAPH GRID

g_col1, g_col2, g_col3 = st.columns([1.2, 1, 1])

with g_col1:
    st.markdown('<div class="chart-slot">', unsafe_allow_html=True)
    st.markdown("### Revenue Generation by Product")
    prod_sales = filtered_df.groupby('Product')['TotalPrice'].sum(
    ).reset_index().sort_values(by='TotalPrice', ascending=True)

    bar_colors = ["#35F35E" if str(p).strip().lower(
    ) == 'chair' else "#2D3139" for p in prod_sales['Product']]

    fig_bar = px.bar(prod_sales, x='TotalPrice', y='Product', orientation='h')
    fig_bar.update_traces(marker_color=bar_colors, texttemplate='$%{x:,.0f}', textposition='outside', textfont=dict(
        color='#FFFFFF'), cliponaxis=False)
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, visible=False), yaxis=dict(showgrid=False, tickfont=dict(color='#FFFFFF', size=11)),
        margin=dict(l=80, r=60, t=10, b=10), height=300
    )
    st.plotly_chart(fig_bar, use_container_width=True,
                    config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

with g_col2:
    st.markdown('<div class="chart-slot">', unsafe_allow_html=True)
    st.markdown("### Order Status Volumes")
    status_counts = filtered_df['OrderStatus'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    status_counts = status_counts.sort_values(by='Count', ascending=True)

    status_colors = {
        'delivered': "#28F815",
        'shipped': "#3E76D1",
        'cancelled': "#FF1818",
        'returned': "#D66929"
    }
    colors_mapped = [status_colors.get(
        str(s).lower(), "#31D9E6") for s in status_counts['Status']]

    fig_status = px.bar(status_counts, x='Count', y='Status', orientation='h')
    fig_status.update_traces(marker_color=colors_mapped, texttemplate='%{x:,}', textposition='outside', textfont=dict(
        color='#FFFFFF', size=11), cliponaxis=False)
    fig_status.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, visible=False), yaxis=dict(showgrid=False, tickfont=dict(color='#FFFFFF', size=12)),
        margin=dict(l=80, r=60, t=10, b=10), height=300
    )
    st.plotly_chart(fig_status, use_container_width=True,
                    config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)


with g_col3:
    st.markdown('<div class="chart-slot">', unsafe_allow_html=True)
    st.markdown("### Coupon Code Utilization")
    filtered_df['CouponCode'] = filtered_df['CouponCode'].fillna(
        'Direct (No Coupon)')
    coupon_counts = filtered_df['CouponCode'].value_counts().reset_index()
    coupon_counts.columns = ['Coupon', 'Volume']

    # Sort data descending so the largest value (FREESHIP) is at the top of the dataframe
    coupon_counts = coupon_counts.sort_values(
        by='Volume', ascending=False).head(5)

    # Custom colors matching your labels perfectly
    faded_purples = ["#FFF019", "#E045B2", "#7329EB", "#35AD7F", '#E9D5FF']

    # FIX: Pass layout structure control parameters directly inside px.pie
    fig_donut = px.pie(
        coupon_counts,
        values='Volume',
        names='Coupon',
        hole=0.5,
        color_discrete_sequence=faded_purples
    )

    # Clean styling controls
    fig_donut.update_traces(
        textposition='outside',
        textinfo='percent+label',
        textfont=dict(color='#FFFFFF', size=11),
        marker=dict(line=dict(color="#1A1C23", width=2)),
        direction='counterclockwise',
        sort=False,
        rotation=90
    )
    fig_donut.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', showlegend=False,
        margin=dict(l=40, r=40, t=10, b=10), height=300
    )
    st.plotly_chart(fig_donut, use_container_width=True,
                    config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)


# 7. ROW 2: FULL-WIDTH CONTINUOUS TIMELINE

st.write("")
st.markdown('<div class="chart-slot">', unsafe_allow_html=True)
st.markdown("### Revenue Performance over Years & Months")

trend_df = filtered_df.copy()
trend_df['Period'] = trend_df['year'].astype(
    str) + "-" + trend_df['month'].astype(str).str.zfill(2)
monthly_revenue = trend_df.groupby(
    'Period')['TotalPrice'].sum().reset_index().sort_values('Period')

fig_line = px.line(monthly_revenue, x='Period', y='TotalPrice')
fig_line.update_traces(line=dict(color='#58A6FF', width=4), mode='lines+markers',
                       marker=dict(size=7, color='#58A6FF', line=dict(width=2, color='#1A1C23')))
fig_line.update_layout(
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(showgrid=False, tickangle=-45,
               tickfont=dict(color='#A0AEC0'), title="Chronological Period"),
    yaxis=dict(showgrid=True, gridcolor='#2D3139', tickfont=dict(
        color='#A0AEC0'), title="Gross Ingestion Revenue ($)"),
    margin=dict(l=50, r=30, t=15, b=40), height=300
)
st.plotly_chart(fig_line, use_container_width=True,
                config={'displayModeBar': False})
st.markdown('</div>', unsafe_allow_html=True)

# 8. STRATEGIC EXECUTIVE RECOMMENDATIONS

st.write("")
st.markdown("### Data-Driven Operational Recommendations")
st.markdown(
    """
    <div style="background-color: #1A1C23; border-left: 4px solid #58A6FF; padding: 18px; border-radius: 6px; border: 1px solid #362B52; border-left-width: 4px;">
        <ul style="margin: 0; padding-left: 20px; color: #E2E8F0; line-height: 1.7;">
            <li><b>Payment Framework Friction Reduction:</b> Because online payment solutions generate our primary pipeline revenue velocity, optimize our digital check-out gateways to simplify conversion steps and minimize friction points.</li>
            <li><b>Targeted Acquisition Scaling:</b> Expand digital promotion investments specifically through the <b>Instagram</b> channel, as the active referral trends highlight this vector as a key driver of digital store customer acquisition.</li>
            <li><b>Logistics Bottleneck Mitigation:</b> Review variations in the horizontal Order Status distribution grid. Sudden increases in cancelled or returned transactions indicate baseline inventory or fulfillment gaps that require immediate handling.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)
