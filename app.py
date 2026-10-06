import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="EEHC Smart Grid & GIS Roadmap Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Modern Styling
st.markdown("""
    <style>
    /* Global styles */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Header Card Styling */
    .main-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        color: white;
        padding: 24px 32px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        color: #FFFFFF !important;
        margin: 0;
        font-size: 2.2rem;
        font-weight: 700;
    }
    .main-header p {
        color: #94A3B8;
        margin-top: 6px;
        font-size: 1rem;
    }

    /* Metric Cards */
    .metric-card {
        background: white;
        padding: 16px;
        border-radius: 8px;
        border-left: 4px solid #0EA5E9;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    .metric-title {
        color: #64748B;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
    }
    .metric-value {
        color: #0F172A;
        font-size: 1.25rem;
        font-weight: 700;
        margin-top: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Data Structure Definitions
DOMAINS = {
    "1. Policy & Regulatory Support": {
        "projects": {
            "PS1": "Policy and regulatory review",
            "PS2": "Technical standards and regulation",
            "PS3": "Privacy and customer data ownership",
            "PS4": "Cybersecurity"
        }
    },
    "2. Organizational Support": {
        "projects": {
            "OS1": "Business goals and use cases",
            "OS2": "Organizational KPIs",
            "OS3": "Asset management strategy",
            "OS4": "Smart grid governance"
        }
    },
    "3. Infrastructure": {
        "projects": {
            "IF1": "Smart meters: commercial and industrial",
            "IF2": "Asset management design and implementation (GIS)",
            "IF3": "Smart meters: residential >200 kWh/month",
            "IF4": "Asset management and monitoring",
            "IF5": "Smart Meter Plus: residential <200 kWh/month",
            "IF6": "Phasor measurement units"
        }
    },
    "4. Technology": {
        "projects": {
            "TE1": "Technology evaluation and selection",
            "TE2": "Integrated solution selection",
            "TE3": "Smart meter analytics",
            "TE4": "PV and EV monitoring",
            "TE5": "Demand response",
            "TE6": "Demand-side management pilot",
            "TE7": "Energy storage pilots"
        }
    },
    "5. Customer Engagement & Environment": {
        "projects": {
            "C1": "Green DISCO",
            "C2": "AMI lessons learned",
            "C3": "Buy REN@DISCO",
            "C4": "Advanced smart meter analytics",
            "C5": "Interactive energy applications"
        }
    }
}

# 4. State Management
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = "Dashboard Home"

def select_project(code):
    st.session_state.selected_project = code

# 5. Navigation Sidebar
with st.sidebar:
    st.title("⚡ EEHC Navigation")
    st.markdown("**Egyptian Electricity Holding Company**\n9 Distribution Companies (DISCOs)")
    st.divider()
    
    if st.button("🏠 Roadmap Dashboard", use_container_width=True, type="primary" if st.session_state.selected_project == "Dashboard Home" else "secondary"):
        select_project("Dashboard Home")
        st.rerun()

    st.subheader("Project Selector")
    for domain_name, domain_info in DOMAINS.items():
        with st.expander(domain_name, expanded=False):
            for code, name in domain_info["projects"].items():
                btn_label = f"🟢 {code}: {name}" if code == "IF2" else f"{code}: {name}"
                if st.button(btn_label, key=f"side_{code}", use_container_width=True):
                    select_project(code)
                    st.rerun()

# 6. Main Dashboard View
if st.session_state.selected_project == "Dashboard Home":
    
    st.markdown("""
        <div class="main-header">
            <h1>Smart Grid Roadmap</h1>
            <p>5 Domains • 26 Projects • 9 Potential Benefits | EEHC and Egypt's nine DISCOs</p>
        </div>
    """, unsafe_allow_html=True)

    cols = st.columns(5)
    
    for i, (domain_name, domain_data) in enumerate(DOMAINS.items()):
        with cols[i]:
            st.markdown(f"### {domain_name.split('.')[1].strip()}")
            st.caption(f"{len(domain_data['projects'])} Projects")
            
            for code, title in domain_data["projects"].items():
                if code == "IF2":
                    st.info(f"**{code}**\n{title}")
                    if st.button(f"Open {code} →", key=f"dash_{code}", use_container_width=True, type="primary"):
                        select_project(code)
                        st.rerun()
                else:
                    if st.button(f"**{code}**\n{title[:26]}...", key=f"dash_{code}", use_container_width=True, help=title):
                        select_project(code)
                        st.rerun()

    st.divider()

    st.subheader("Potential Benefits of the Smart-Grid Portfolio")
    
    b_cols = st.columns(3)
    with b_cols[0]:
        st.markdown("""
        * **B1:** Deferred grid investment[cite: 1]
        * **B2:** Avoided grid investment[cite: 1]
        * **B3:** Reduced electricity losses[cite: 1]
        """)
    with b_cols[1]:
        st.markdown("""
        * **B4:** Reduced planned outages[cite: 1]
        * **B5:** Reduced unplanned outages[cite: 1]
        * **B6:** Improved customer satisfaction[cite: 1]
        """)
    with b_cols[2]:
        st.markdown("""
        * **B7:** Reduced CO₂ emissions[cite: 1]
        * **B8:** Improved organizational efficiency[cite: 1]
        * **B9:** EV integration benefits[cite: 1]
        """)

# 7. GIS Project Page (IF2: Asset Management Design & Implementation)
elif st.session_state.selected_project == "IF2":
    
    st.button("← Back to Smart Grid Roadmap", on_click=select_project, args=("Dashboard Home",))
    
    st.title("🗺️ IF2: Asset Management Design & Implementation (GIS Rollout)")
    st.caption("Strategic Roadmap & Operational Implementation for EEHC and 9 Distribution Companies")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card"><div class="metric-title">Coverage Target</div><div class="metric-value">100% MV Network</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><div class="metric-title">Target Horizon</div><div class="metric-value">June 2027</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><div class="metric-title">Participating Entities</div><div class="metric-value">9 DISCOs</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><div class="metric-title">Core Engine</div><div class="metric-value">ArcGIS & Enterprise</div></div>', unsafe_allow_html=True)

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(["🚀 Implementation Roadmap", "🏛️ Delivery & Architecture", "🗺️ Horizon Timeline", "📊 Monitoring & Outcomes"])

    with tab1:
        st.subheader("GIS Rollout Journey")
        st.markdown("""
        * **Central Foundation:** Upgraded ArcGIS Pro / Enterprise & SQL integration[cite: 1].
        * **Smouha Proof of Concept:** Initial validation performed with a trained 7-person R&D team[cite: 1].
        * **MV Network Coverage (By June 2027):** Mapping and full acceptance of Medium Voltage network records[cite: 1].
        * **LV Coverage & Operating Apps (To May 2030):** Extending network records to Low Voltage and deploying apps (OMS, Asset Maintenance, Field Workforce)[cite: 1].
        """)

    with tab2:
        st.subheader("Joint Delivery Team & Integration Readiness")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### Readiness Routes for DISCOs")
            st.markdown("""
            1. **Established GIS:** Synchronize local tool updates to central SQL database[cite: 1].
            2. **Partial / Fragmented GIS:** Consolidate data, fill gaps, and provide field drawing equipment[cite: 1].
            3. **No GIS:** Perform complete component survey and use the central platform[cite: 1].
            """)
        with col_b:
            st.markdown("#### Joint Delivery Model")
            st.markdown("""
            * **EEHC GIS / R&D Team:** Common standard model, SQL publication, support[cite: 1].
            * **DISCOs Network & Control:** Field identification, location verification, update ownership[cite: 1].
            * **Joint Acceptance Team:** Coordinates, attributes, and connectivity checks[cite: 1].
            """)

    with tab3:
        st.subheader("Three Delivery Horizons")
        st.markdown("""
        | Horizon | Timeline | Core Focus | Key Evidence to Advance |
        | :--- | :--- | :--- | :--- |
        | **Short Term** | Jan 2026 – Jun 2027 | Central Foundation & MV Network Coverage | Accepted MV records across all 9 DISCOs[cite: 1] |
        | **Medium Term** | Jun 2027 – May 2030 | LV Coverage & Operational Applications | Validated electrical models & measured value[cite: 1] |
        | **Long Term** | May 2030 Onward | Coordinated Operations (ADMS, AMI, Peak) | Approved investment cases & operating readiness[cite: 1] |
        """)

    with tab4:
        st.subheader("Continuous Update Workflow & Sector Outcomes")
        st.markdown("""
        **Data Lifecycle Pipeline:**
        `1. Capture (Field Change)` ➔ `2. Verify (DISCO Lead)` ➔ `3. Approve (QA Checklist)` ➔ `4. Publish (SQL/GIS Dashboard)`[cite: 1]
        """)

# 8. Dynamic View for Other Projects
else:
    st.button("← Back to Smart Grid Roadmap", on_click=select_project, args=("Dashboard Home",))
    
    code = st.session_state.selected_project
    project_title = "Selected Project"
    for d in DOMAINS.values():
        if code in d["projects"]:
            project_title = d["projects"][code]

    st.title(f"📌 {code}: {project_title}")
    st.info("This project module is currently scheduled for deployment. The interactive workspace below is reserved.")

    st.markdown(f"""
    ### Project Overview
    * **Project Code:** `{code}`
    * **Project Title:** {project_title}
    * **Status:** Draft / Reserved Space
    """)
    
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Project Lead", placeholder="Assign lead...")
        st.selectbox("Project Phase", ["Planning", "Pilot Execution", "Rollout", "Completed"])
    with c2:
        st.date_input("Target Start Date")
        st.text_area("Notes & Scope Definition", placeholder="Enter specific scope requirements...")

    st.button("Save Configuration", type="primary")
