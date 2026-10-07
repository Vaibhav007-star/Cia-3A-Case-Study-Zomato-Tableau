# CIA IIIB: PRESENTATION SLIDE DECK
## BEYOND THE 5-STAR TRAP: A MULTI-CRITERIA RESTAURANT RELEVANCE & DISCOVERY ENGINE ON ZOMATO
**Student Presentation Deck | Total Duration: 10 Minutes | Evaluation: 20 Marks**  
**Companion Artifacts:** [`CIA_IIIB_Zomato_Case_Study_Report.md`](file:///c:/Projects/Zomotao/CIA_IIIB_Zomato_Case_Study_Report.md) & [`Zomato_Star_Schema.png`](file:///c:/Projects/Zomotao/Zomato_Star_Schema.png)

---

## SLIDE 1: TITLE & PROJECT BRIEF
* **Title:** Beyond the 5-Star Trap: A Multi-Criteria Restaurant Discovery & Relevance Framework on Zomato
* **Topic:** Data Warehousing, ETL, Dimensional Modeling (Star Schema), OLAP & Business Intelligence
* **Context:** Hyperlocal Food Aggregator Analytics (Delhi-NCR Market: 7,947 Restaurants)
* **Presenter:** Student Team / Individual Candidate
* **Speaking Notes (1 min):**
  > "Good morning, respected evaluators. Today, I am presenting our Business Intelligence case study for Zomato. We address a critical platform dilemma: consumer choice overload and the market distortions created by simple one-dimensional sorting mechanisms. We propose an end-to-end BI solution comprising an automated ETL pipeline, an enterprise Kimball Star Schema, and an interactive Tableau Public decision-support simulator."

---

## SLIDE 2: BUSINESS PROBLEM & CHOICE OVERLOAD
* **The Problem:** In Delhi-NCR, users face 7,947 dining options, triggering cognitive choice overload (*Schwartz, 2004*).
* **Failure Mode 1 (The Popularity Trap):**
  * Review counts follow an extreme power law: median = 19 votes, 99th percentile = 1,590.
  * Sorting strictly by votes promotes expensive legacy chains (mean cost ₹1,470 vs median ₹450), where **70% lack online home delivery**.
* **Failure Mode 2 (The 5-Star Fallacy):**
  * Sorting strictly by raw rating elevates niche venues with small samples while ignoring diner budgets.
* **Failure Mode 3 (Hidden Gem Invisibility):**
  * 194 elite restaurants ($\ge 4.0$ rating) with 53.6% delivery readiness remain buried due to low historical votes ($< 200$).
* **Speaking Notes (1.5 min):**
  > "When consumers search on food platforms, defaulting to 'Sort by Popularity' concentrates exposure onto legacy chains with double the market price, many of which don't even deliver food to homes. Meanwhile, 194 exceptional local restaurants with higher delivery readiness remain invisible on page 10+ of search results. Our BI project solves this marketplace failure."

---

## SLIDE 3: DATA ARCHITECTURE & ETL DATA QUALITY PIPELINE
* **Data Sources Integrated:**
  1. Primary OLTP Restaurant Listing Extract (9,551 records)
  2. Master Geopolitical Lookup (`Country-Code.xlsx` - 15 sovereign countries)
  3. Spatial Municipal Neighborhood Classification (Delhi-NCR)
* **Data Quality Engineering Transformations:**
  * **Missing Values:** Imputed 9 missing cuisines as 'Not Specified'.
  * **Outliers:** Imputed 18 zero-cost records via hierarchical median ($\text{City} \times \text{Price Tier}$).
  * **Cold-Start Isolation:** Created `Is_Rated` flag to isolate 2,139 unrated (0.0★) listings.
  * **Log Transformation:** Applied $\ln(1 + \text{Votes})$ to compress power-law review skew.
  * **Spatial Validation:** Flagged 497 (0,0) coordinate anomalies with `Has_Valid_Coordinates`.
* **Speaking Notes (1.5 min):**
  > "Real-world data is dirty. Our Python ETL pipeline rectified missing cuisines, zero-cost anomalies, and coordinate errors. Crucially, we didn't blindly delete 2,139 unrated restaurants—we flagged them as cold-start entries to prevent distorting our rating benchmarks while preserving the onboarding pipeline."

---

## SLIDE 4: DIMENSIONAL MODELING — THE STAR SCHEMA
*(Display graphic: `Zomato_Star_Schema.png`)*
* **Fact Table:** `FACT_RESTAURANT_PERFORMANCE`
  * **Grain:** Exactly 1 record per physical restaurant outlet profile per snapshot.
  * **Additive Measures:** `Listing_Count` ($=1$), `Votes`, `Average_Cost_Clean`.
  * **Semi-Additive/Non-Additive:** `Aggregate_Rating`, `Log_Votes`, `Relevance_Score`.
* **Conformed Dimension Tables (Surrogate Keys):**
  * `DIM_RESTAURANT` (Natural key, chain status, outlet count)
  * `DIM_LOCATION` (Locality, City, Country, spatial coordinates)
  * `DIM_CUISINE` (Primary cuisine, category, cuisine count)
  * `DIM_SERVICE_PROFILE` (Online delivery, table booking, active dispatch)
  * `DIM_PRICE_TIER` (Price range 1–4, currency, budget classification)
  * `DIM_RESTAURANT_SEGMENT` (LOD segment, rating status, strategic action)
* **Speaking Notes (2 min):**
  > "Following Ralph Kimball's methodology, our Star Schema centers on `FACT_RESTAURANT_PERFORMANCE` with a grain of one row per restaurant outlet. By indexing foreign surrogate keys to 6 conformed dimensions, we achieve lightning-fast OLAP query performance and eliminate runtime table joins in Tableau."

---

## SLIDE 5: MULTI-DIMENSIONAL OLAP OPERATIONS
* **Roll-Up:** Granular Outlets $\rightarrow$ Localities (e.g., GK-1) $\rightarrow$ Metro Cities $\rightarrow$ National Market.
* **Drill-Down:** Navigating from executive city totals into granular neighborhood streets.
* **Slice:** Filtering the warehouse exclusively to the **Delhi-NCR Metro Market ($N = 7,947$)**.
* **Dice:** Intersecting $[\text{Budget Tier 1}] \times [\text{North Indian}] \times [\text{Online Delivery = Yes}]$.
* **Pivot:** Cross-tabulating Price Tiers across Columns and Rating Bands across Rows (Highlight Heatmap).
* **Speaking Notes (1 min):**
  > "This dimensional structure allows multi-dimensional OLAP analysis: rolling up from street stalls to metro averages, drilling down into specific localities, slicing the Delhi-NCR market, and dicing across cuisines and budget constraints."

---

## SLIDE 6: THE RESTAURANT RELEVANCE SCORING MODEL
* **Formula:**
  $$\text{Relevance Score} = \frac{w_r \cdot S_{\text{rating}} + w_e \cdot S_{\text{engagement}} + w_a \cdot S_{\text{affordability}} + w_s \cdot S_{\text{service}}}{\sum w_i}$$
* **Component Utility Functions (0–100 Scale):**
  1. **Quality ($S_{\text{rating}}$):** $(\text{Aggregate\_Rating} / 5.0) \times 100$
  2. **Social Proof ($S_{\text{engagement}}$):** $(\ln(1 + \text{Votes}) / 8.9787) \times 100$
  3. **Continuous Budget Fit ($S_{\text{affordability}}$):** 100 if Cost $\le$ Budget; continuous linear penalty for overages up to $2\times$ Budget; 0 beyond.
  4. **Service Utility ($S_{\text{service}}$):** $20 \text{ base} + 50 \text{ (Delivery)} + 30 \text{ (Table Booking)}$.
* **Speaking Notes (1.5 min):**
  > "Rather than using an opaque black-box machine learning model, we designed a transparent multi-attribute utility score. Each factor is normalized from 0 to 100. Diners can adjust their priority weights dynamically, and budget overages are penalized smoothly rather than abruptly cutting off options."

---

## SLIDE 7: TABLEAU PUBLIC DASHBOARDS & LAB MANUAL ALIGNMENT
* **Dashboard 1: Ecosystem & Spatial Overview (1366x768):**
  * Executive BAN Cards, Dual-Axis Spatial Map (Lab 4), Cuisine Treemap (Lab 6), Cost Histogram (Lab 3).
* **Dashboard 2: Strategic Segmentation (LOD Analysis):**
  * Log-Votes vs. Rating Scatter, Fixed LOD Locality Benchmark (Lab 7.2), Price-Rating Matrix (Lab 6).
* **Dashboard 3: Personalized Ranking Simulator:**
  * Interactive Parameter Sliders (`p Budget`, `p Preset`, `p Top N`), Ranked Top-N Table (Lab 7.1 & 7.3), Score Decomposition Stacked Bar.
* **Speaking Notes (1.5 min):**
  > "Our Tableau workbook directly implements the Advanced Dashboard Lab Manual: Fixed LOD expressions for neighborhood benchmarks, dual-axis spatial maps, parameter controls, and dynamic What-If table calculations. As user budget parameters change, rankings recalculate live."

---

## SLIDE 8: EMPIRICAL RESULTS & TOP 10 COMPARISON

| Metric | Traditional Sort (By Votes) | Proposed Relevance Engine | Business Impact |
| :--- | :---: | :---: | :--- |
| **Average Cost for Two** | **₹1,470** | **₹515** | **64.9% Cost Reduction** (Fits ₹800 budget) |
| **Online Delivery Availability** | **30.0% (3/10)** | **100.0% (10/10)** | **+70% Delivery Readiness** |
| **Average Customer Rating** | **4.25 / 5.0** | **4.28 / 5.0** | **Quality Standards Preserved** |
| **Top 10 List Overlap** | Reference | **10% (1 out of 10)** | **90% Novel High-Utility Discoveries** |

* **Speaking Notes (1 min):**
  > "Here is the empirical proof: Under an ₹800 budget constraint, our framework drops the average dining cost from ₹1,470 down to ₹515—a 64.9% savings—while achieving 100% home delivery readiness and maintaining an elite 4.28 rating. Nine out of ten recommended venues are fresh, accessible discoveries."

---

## SLIDE 9: STRATEGIC BUSINESS RECOMMENDATIONS
1. **Dynamic Multi-Slider Filters:** Replace static sorting with user-controlled priority sliders (Expected: 12% drop in session bounce rate).
2. **"Hidden Gem" Algorithmic Carousels:** Feature top-rated local venues with an engagement threshold of $N \ge 30$ votes (Expected: 20% first-order lift for new merchants).
3. **Intent-Decoupled Discovery Feeds:** Separate Dine-Out discovery from Online Delivery discovery to prevent delivery order drop-off.
4. **"Exceptional Value" Badging:** Award badges to venues achieving rating $\ge 4.0$ with cost below their locality LOD average.
* **Speaking Notes (1 min):**
  > "From a business perspective, these insights translate directly into revenue: multi-slider search reduces cart abandonment, intent-based feeds boost delivery checkout, and promoting hidden gems prevents newly onboarded restaurant churn."

---

## SLIDE 10: LIMITATIONS, FUTURE SCOPE & CONCLUSION
* **Academic Integrity & Limitations:**
  * Static cross-sectional dataset without transaction timestamps.
  * Prototype is an interpretable decision support system, not a replica of Zomato's proprietary production algorithm.
* **Future Production Roadmap:**
  * Real-time GPS distance matrix and kitchen prep dispatch telemetry.
  * Supervised learning re-ranker trained on user clickstream logs.
* **Conclusion:**
  * Successfully demonstrated how dimensional modeling, ETL engineering, and Business Intelligence can transform restaurant discovery and resolve marketplace choice overload.
* **Speaking Notes (0.5 min):**
  > "To conclude, this project bridges academic data warehousing theory and real-world business intelligence to solve consumer choice overload. We are now open for questions and viva defense. Thank you!"

---
*Generated for University Evaluation:* [`CIA_IIIB_Zomato_Case_Study_Report.md`](file:///c:/Projects/Zomotao/CIA_IIIB_Zomato_Case_Study_Report.md)  
*Architectural Graphic Reference:* [`Zomato_Star_Schema.png`](file:///c:/Projects/Zomotao/Zomato_Star_Schema.png)

