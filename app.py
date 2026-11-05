# ============================================================
# RASHED ABDULLAH
# CIVIL ENGINEERING PORTFOLIO
# FLASK APPLICATION
# ============================================================

from flask import Flask, render_template


# ============================================================
# CREATE FLASK APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# PROJECT 01
# EQUIPMENT RENT VS. BUY DECISION TOOL
# ============================================================

@app.route("/rent-vs-buy")
def rent_vs_buy():
    return render_template("rent_vs_buy.html")


# ============================================================
# PROJECT 02
# SAP2000 SEISMIC & STRUCTURAL ANALYSIS
# ============================================================

@app.route("/structural-analysis")
def structural_analysis():
    return render_template("structural_analysis.html")


# ============================================================
# PROJECT 03
# MILITARY HOSPITAL CONSTRUCTION PROJECT
# ============================================================

@app.route("/military-hospital")
def military_hospital():
    return render_template("military_hospital.html")


# ============================================================
# PROJECT 04
# I-5 / SR-14 EARTHQUAKE FAILURE INVESTIGATION
# ============================================================

@app.route("/forensic-engineering")
def forensic_engineering():
    return render_template("forensic_engineering.html")


# ============================================================
# PROJECT 05
# GIS FLOOD RISK ASSESSMENT
# HARRIS COUNTY, TEXAS
# ============================================================

@app.route("/gis-flood-risk")
def gis_flood_risk():
    return render_template("gis_flood_risk.html")


# ============================================================
# PROJECT 06
# MODEL-BASED RESIDENTIAL COST ESTIMATION
# ============================================================

@app.route("/residential-cost-estimation")
def residential_cost_estimation():
    return render_template("residential_cost_estimation.html")


# ============================================================
# RUN FLASK DEVELOPMENT SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )