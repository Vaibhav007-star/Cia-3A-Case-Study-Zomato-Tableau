# BEYOND THE 5-STAR TRAP: A MULTI-CRITERIA RESTAURANT RELEVANCE & DISCOVERY ENGINE ON ZOMATO
## Applied Business Intelligence & Analytics Case Study

---

## Executive Summary
This project investigates the widespread phenomenon of **"choice overload"** in two-sided food delivery and dining platforms, specifically focusing on Zomato. In high-density dining markets such as the Delhi-National Capital Region (NCR), users faced with thousands of restaurants default to simple sorting mechanisms (such as "Sort by Popularity" or "Sort by Rating"). 

Through empirical evaluation of 9,551 global restaurants (8,652 in India), we demonstrate that these one-dimensional sorting approaches create severe market distortions:
1. **The Popularity Bias**: Sorting by review volume concentrates discovery around legacy mega-chains (mean cost ₹1,400), of which 50% do not offer online home delivery.
2. **The 5-Star Trap**: Sorting solely by rating elevates low-review venues with unverified sample sizes or obscures affordable dining.
3. **The Hidden Gem Invisibility**: Over 483 restaurants possess ratings $\ge 4.0$ but review volumes $< 200$, leaving them buried on page 10+ of platform search results.

To address this, we developed a transparent, user-tunable **Multi-Criteria Relevance Framework** implemented as a prototype in Tableau Public. The framework normalizes Quality (Rating), Social Proof (log-scaled review volume), Budget Compatibility, and Service Availability into a unified 0–100 index. When simulated against an ₹800 budget constraint, our framework shifted the Top 10 recommendations to achieve a **46% cost reduction** (₹755 vs ₹1,400) and **100% online delivery readiness**, while preserving elite customer satisfaction (average rating 4.47 vs 4.53).

---

## 1. Company & Industry Context
* **Company**: Zomato Limited (NSE: ZOMATO / Eternal Ltd.)
* **Industry**: Food Delivery & Hyperlocal Dining Discovery
* **Scale**: Millions of transacting users and hundreds of thousands of active merchant restaurant partners.
* **Problem Landscape**: In hyper-dense urban agglomerations, food discovery platforms face a dual challenge: maximizing consumer conversion while maintaining an equitable merchant marketplace where quality restaurants are discoverable.

---

## 2. Problem Statement
> *"How can Zomato mitigate consumer choice overload and search abandonment by transitioning from one-dimensional popularity rankings to an interpretable, multi-criteria relevance framework that dynamically aligns with user budget, quality expectations, and service constraints?"*

---

## 3. Empirical Research: Fact vs. Inference vs. Proposed Solution

### A. FACT (Documented by Industry & Literature)
* Two-sided food aggregators report that search abandonment increases when users are presented with unranked or poorly matched options (Schwartz, 2004 *The Paradox of Choice*).
* User review counts follow an extreme power-law distribution, where top 5% of restaurants monopolize over 70% of platform engagement.
* Zomato Engineering publicly emphasizes that discovery ranking must balance relevance, merchant distance, kitchen prep time, and customer preferences.

### B. INFERENCE (Derived from Exploratory Analysis)
* Default platform ranking mechanisms driven primarily by total review count inherently favor long-standing incumbent establishments over newly emerging high-quality culinary ventures.
* High average spend does not correlate with superior customer satisfaction; in fact, mid-tier and budget offerings demonstrate equal or superior median ratings.

### C. OUR PROPOSED SOLUTION
* A transparent, multi-attribute utility framework accessible in Tableau that allows real-time parameter tuning:
  $$\text{Relevance Score} = w_r \cdot \text{Rating} + w_e \cdot \ln(1 + \text{Votes}) + w_a \cdot \text{Affordability} + w_s \cdot \text{Service}$$

---

## 4. Dataset Evaluation & Data Cleaning Pipeline
The analysis is grounded in the Zomato multi-city dataset consisting of 9,551 records across 15 countries, with 8,652 observations focused in India.

### Data Cleaning Actions Taken:
1. **Handling 2,148 Unrated Records**: 22.5% of rows exhibited `Aggregate rating = 0.0` with `Rating text = 'Not rated'`. These were isolated via an `Is_Rated` flag to prevent downward rating bias.
2. **Log-Scaling of Engagement**: Review votes ranged from 0 to 10,934 with a median of 31. Natural log-scaling was applied to eliminate power-law compression.
3. **Imputation of Missing Values**: 9 null cuisine fields were imputed as `'Not Specified'`; 18 zero costs were imputed using city-level median cost within the respective price tier.
4. **Primary Cuisine Extraction**: Parsed multi-label strings (1,825 unique combinations) into primary cuisine categories.

---

## 5. Strategic Restaurant Segmentation Matrix

| Segment Name | Definition Criteria | Record Count | Strategic Business Role |
| :--- | :--- | :--- | :--- |
| **Market Leaders** | Rating $\ge 4.0$ & Votes $\ge 200$ | **897** | Brand anchors; high platform GMV drivers. |
| **Hidden Gems** | Rating $\ge 4.0$ & Votes $< 200$ | **483** | High customer delight; require platform discovery boost. |
| **Popular Volume Drivers** | Rating $3.0 - 3.9$ & Votes $\ge 200$ | **773** | High transaction volume; operational improvement candidates. |
| **Average Performers** | Rating $3.0 - 3.9$ & Votes $< 200$ | **3,817** | Core neighborhood dining options. |
| **Underperformers** | Rating $> 0$ & Rating $< 3.0$ | **1,433** | Merchant partner retention and quality intervention needed. |
| **Unrated / New Entrants** | Rating $= 0.0$ | **2,148** | Cold-start incubation pipeline. |

---

## 6. Quantitative Evaluation: Traditional vs. Proposed Framework

Simulating user preferences with a **Budget Constraint of ₹800** and default weights (Rating 40%, Popularity 25%, Affordability 20%, Service 15%):

| Metric | Traditional Sort (By Votes) | Proposed Relevance Engine | Business Impact |
| :--- | :--- | :--- | :--- |
| **Average Top 10 Rating** | 4.53 / 5.0 | **4.47 / 5.0** | Maintained elite quality standards ($\Delta -0.06$). |
| **Average Top 10 Cost for Two** | ₹1,400 | **₹755** | **46.1% reduction in dining expense**; fits budget. |
| **Online Delivery Availability** | 50.0% | **100.0%** | **2x increase in immediate order conversion**. |
| **Table Booking Availability** | 30.0% | **80.0%** | High utility dining reservations. |
| **Top 10 List Overlap** | — | **1 out of 10** (*Truffles*) | **9 new high-utility restaurants surfaced**. |

---

## 7. Actionable Business Recommendations

1. **Implement "Hidden Gem Badging" on Discovery Feed**:
   - *Problem*: 483 high-rated restaurants suffer low order volumes due to low review count.
   - *Action*: Feature an algorithmic carousel "Top Rated Local Gems" with a lower review threshold ($N \ge 30$).
   - *KPI*: 15% increase in first-time merchant order conversions.

2. **Dynamic Multi-Slider Filters in Mobile UI**:
   - *Problem*: Static single-column sorting creates search abandonment.
   - *Action*: Allow users to toggle priority weights (e.g., "Prioritize Budget" vs "Prioritize Quality").
   - *KPI*: 12% reduction in search session drop-off.

3. **Merchant Service Optimization Advisory**:
   - *Problem*: Restaurants offering only dine-in miss high-relevance ranking opportunities.
   - *Action*: Provide merchant analytics dashboards demonstrating that onboarding delivery increases relevance visibility by 25%.
   - *KPI*: 8% uplift in merchant delivery fleet adoption.

---

## 8. Limitations & Academic Integrity
* **Observational Snapshot**: The dataset represents cross-sectional public restaurant profiles and does not include user session clickstream, real-time geolocation GPS vectors, or live kitchen dispatch queues.
* **Algorithmic Scope**: This project is an interpretable decision support prototype, not a replication of Zomato's proprietary machine learning recommender.

