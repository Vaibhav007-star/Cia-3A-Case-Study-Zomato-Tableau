You are my expert Tableau consultant, data analyst, business-case researcher, and academic project mentor.

I am a B.Sc. Data Science & AI student working on a university assignment in which I must create a **real-life case study and solve a genuine business problem using Tableau**.

I have attached:
1. My university's **Advanced Dashboard Lab Manual**
2. The **Zomato dataset** that I intend to use

You MUST use the attached lab manual as the primary reference for the Tableau techniques, terminology, and level of complexity expected in my course. Do not ignore the manual or replace its techniques with unrelated methods.

My goal is to create a project that is:
- Based on a genuine real-world business problem
- Supported by research
- Data-driven
- Solved through a practical analytical framework
- Interactive in Tableau
- More advanced than a basic classroom dashboard
- Strong enough to present as a serious case study
- Technically achievable by a university student
- Honest about the limitations of the available data

## PROJECT DIRECTION

The case study is about Zomato and restaurant discovery.

The broad problem we are investigating is:

### “Choice overload in restaurant discovery”

A user searching for food on a platform such as Zomato may have a very large number of restaurants to choose from. Simply ranking restaurants by one metric such as rating, popularity, or price may not produce the most relevant result for every user.

Zomato has publicly discussed search, restaurant ranking, relevance, contextual signals, and personalization as real product/data-science challenges.

However, I do NOT want to falsely claim that we are reproducing Zomato's proprietary production recommendation system.

Instead, our project should be positioned as:

### “A Tableau-based prototype for improving restaurant discovery through a transparent, preference-based restaurant ranking framework using publicly available restaurant data.”

The exact final project title can be improved by you after inspecting the dataset.

---

# MAIN BUSINESS PROBLEM

We need to answer:

### “How can Zomato reduce restaurant choice overload by identifying and prioritizing restaurants that are more relevant to a user's preferences?”

The proposed solution should be an interpretable **Restaurant Relevance Score / Restaurant Ranking Framework** based on variables actually available in the dataset.

Possible dimensions include:
- Restaurant rating
- Customer votes / engagement
- Approximate cost
- Cuisine
- Restaurant type
- Online ordering availability
- Table booking availability
- City
- Locality
- Other useful fields actually present in the dataset

IMPORTANT:
Do not assume a field exists.
First inspect the actual dataset and tell me exactly what fields are available, what they mean, and which ones are reliable enough to use.

---

# YOUR ROLE

Act as my project partner from beginning to end.

You must help me with:

1. Problem formulation
2. Background research
3. Dataset evaluation
4. Data cleaning
5. Feature engineering
6. Analytical methodology
7. Restaurant relevance-score design
8. Tableau calculated fields
9. Parameters
10. Sets
11. Filters
12. Dashboard actions
13. Dashboard layout
14. Interactive controls
15. Insights
16. Business recommendations
17. Report writing
18. Presentation preparation
19. Viva questions
20. Final quality checking

Do not jump straight into dashboard design.

First understand the data and establish whether the proposed problem can genuinely be analyzed with it.

---

# STEP 1 — INSPECT THE DATASET

Start by examining the attached dataset.

Give me:

### A. Dataset overview
- Number of rows
- Number of columns
- Each column name
- Data type
- Approximate number of unique values
- Missing-value percentage
- Important categorical fields
- Important numerical fields

### B. Data-quality problems
Identify:
- Missing values
- Duplicate restaurants
- Duplicate records
- Invalid ratings
- Inconsistent cost values
- Incorrect or inconsistent cuisine names
- Inconsistent city/locality names
- Boolean fields with inconsistent values
- Outliers
- Any other problems

### C. Analytical usefulness
For every important field, explain:
- What business question it can answer
- Whether it should be used
- Whether it needs cleaning
- Whether it is safe for a calculated score

DO NOT fabricate any statistics before inspecting the data.

---

# STEP 2 — VALIDATE THE BUSINESS PROBLEM

After inspecting the dataset, determine whether the dataset is genuinely capable of supporting the problem.

I want you to explicitly answer:

### “Can this dataset support a defensible analysis of restaurant relevance?”

If yes:
- Explain why
- Identify the relevant variables

If only partially:
- Explain the limitations
- Adapt the case study while keeping the core business problem

If no:
- Do not force the idea
- Recommend the strongest alternative Zomato problem supported by the actual dataset

Be academically honest.

---

# STEP 3 — RESEARCH THE REAL-WORLD CASE

Research the real-world context around Zomato's restaurant discovery/search/ranking problem using reliable sources.

Prioritize:
- Zomato's official engineering/product articles
- Zomato/Eternal investor documents where relevant
- Official reports
- Academic research on recommendation/ranking systems
- Reliable industry sources

Use citations for claims.

Separate:
### FACT
What Zomato or a reliable source actually states.

### INFERENCE
What we infer from the available evidence.

### OUR PROPOSED SOLUTION
What we are designing as part of this academic project.

Do NOT invent Zomato internal metrics, algorithms, conversion rates, customer behavior, or proprietary information.

Prepare:
- Background
- Existing problem
- Why the problem matters
- Existing approaches used by the industry
- Gap/limitation in publicly available data
- Our proposed solution

---

# STEP 4 — DEFINE THE FINAL CASE STUDY

Create a strong case-study framework:

## 1. Title

Make it sound professional and analytical.

## 2. Business Problem

One precise paragraph.

## 3. Stakeholder

Clearly identify who would use this solution:
- Zomato product team
- Restaurant-partner team
- Search/discovery team
- Users
etc.

Choose the most logical stakeholder.

## 4. Objective

Define 4–6 measurable objectives.

## 5. Key Questions

Create 5–8 analytical questions that the dashboard must answer.

## 6. Proposed Solution

Clearly explain the Restaurant Relevance Score.

## 7. Expected Impact

Explain what the dashboard is expected to improve.

Do NOT claim actual improvement unless the data allows us to prove it.

---

# STEP 5 — DESIGN THE RESTAURANT RELEVANCE SCORE

This is the central analytical component.

First determine which variables from the actual dataset are appropriate.

Possible components:

### Rating Score
Higher customer rating → higher score

### Engagement/Popularity Score
Higher votes → higher score

### Affordability Score
Restaurants that fit the user's budget → higher score

### Service Availability Score
For example:
Online Ordering
Table Booking

### Preference Match Score
For example:
Cuisine
Restaurant Type
Location

Create a mathematically sensible scoring system.

Potential structure:

Restaurant Relevance Score =
Weighted Rating Score
+ Weighted Engagement Score
+ Weighted Affordability Score
+ Weighted Service Score
+ Weighted Preference Match Score

BUT:

Do not blindly use the weights I suggested.

First analyze the dataset and explain the reasoning for the weights.

Consider normalization because rating, votes and cost are on different scales.

Explain every formula in simple language.

---

# STEP 6 — MAKE THE SCORE INTERACTIVE

I want the Tableau dashboard to allow users to adjust their preferences.

Possible parameters:

### Rating Importance
0–100%

### Price Importance
0–100%

### Popularity Importance
0–100%

### Service Importance
0–100%

### Minimum Rating
3.0–5.0

### Maximum Budget
₹200–₹3000

The exact parameters/ranges should be based on the actual dataset.

Tell me:

- Which parameters are technically feasible in Tableau
- How to create each one
- Exact parameter settings
- Exact calculated-field formulas
- How parameter changes affect the ranking

Where appropriate, use techniques from my lab manual such as:
- Parameters
- LOD expressions
- Sets
- Set actions
- Parameter actions
- Dashboard filter actions
- Top-N analysis
- BAN/KPI cards
- Navigation
- Storytelling

Do not force every technique into the project.

Use only techniques that strengthen the case.

---

# STEP 7 — CREATE RESTAURANT SEGMENTS

Develop a useful segmentation framework based on actual data.

Potential concept:

### Leaders
High rating + high engagement

### Hidden Gems
High rating + relatively low engagement

### Popular but Weak
High engagement + lower rating

### Low Visibility
Low engagement + lower rating

The exact thresholds must be data-driven.

Prefer:
- Percentiles
- Median
- Parameters
- LOD expressions

over arbitrary hard-coded values where appropriate.

Explain exactly how to calculate the segments in Tableau.

---

# STEP 8 — DESIGN THE TABLEAU DASHBOARD

I want approximately 3 connected dashboard pages.

They should tell one continuous story.

## DASHBOARD 1 — EXECUTIVE OVERVIEW

Possible title:
### “Zomato Restaurant Marketplace — Understanding the Choice Problem”

Include:

KPI cards:
- Total Restaurants
- Average Rating
- Average Cost
- Total Votes
- Online Ordering %

Charts such as:
- Restaurant distribution by city
- Rating distribution
- Cost distribution
- Restaurant type distribution
- Cuisine distribution

Purpose:
Establish the scale and complexity of the restaurant marketplace.

---

# DASHBOARD 2 — RESTAURANT PERFORMANCE & SEGMENTATION

Possible title:
### “What Makes a Restaurant Stand Out?”

Main visualization:

## Rating vs Customer Engagement Scatter Plot

X-axis:
Rating

Y-axis:
Votes

Color:
Restaurant Segment

Size:
Cost or another analytically meaningful variable

Add:
- Trend/reference lines where useful
- Tooltips
- Highlight actions
- Selection/filter interactions

Also include:
### Price vs Rating
and/or
### City/Locality × Restaurant Type Heatmap

The page should identify:
- Leaders
- Hidden Gems
- Popular but Weak restaurants
- Low-visibility restaurants

---

# DASHBOARD 3 — THE SOLUTION

Possible title:
### “Personalized Restaurant Ranking Simulator”

This must be the key dashboard.

Include:

## User controls

- Minimum rating
- Maximum budget
- Rating importance
- Price importance
- Popularity importance
- Service preference where feasible

Then dynamically show:

### Top 10 Recommended Restaurants

Fields:
- Rank
- Restaurant
- Rating
- Votes
- Approx Cost
- Cuisine
- Restaurant Type
- Online Order
- Relevance Score

Also include:

### “Why was this restaurant recommended?”

Create a transparent explanation using the score components.

Example concept:

⭐ High rating  
💰 Fits selected budget  
🔥 Strong engagement  
🛵 Online ordering available

Only use explanation fields actually supported by the dataset.

---

# STEP 9 — COMPARE THE NEW SYSTEM WITH SIMPLE POPULARITY RANKING

This is important.

Create:

### Traditional Ranking
Rank restaurants using popularity/votes.

versus

### Proposed Ranking
Rank restaurants using the Relevance Score.

Then analyze:
- How different are the Top 10 lists?
- How many highly rated restaurants appear?
- How many value-for-money restaurants appear?
- How many potentially overlooked restaurants enter the recommendations?

This should provide evidence for whether the proposed ranking framework adds value.

Do not claim the new system is “better” unless the evaluation framework supports that conclusion.

Instead, explain what our analysis demonstrates and what would require a real A/B test on production Zomato data.

---

# STEP 10 — TABLEAU TECHNICAL IMPLEMENTATION

For EVERY worksheet, give me:

### Worksheet name

### Purpose

### Dimensions

### Measures

### Rows shelf

### Columns shelf

### Marks type

### Color

### Size

### Label

### Detail

### Filters

### Parameters

### Calculated fields

### Sort settings

### Tooltip design

### Dashboard action settings

### Exact Tableau steps

For every calculated field, provide the exact Tableau formula in a code block.

Do not give vague instructions such as:
“Create a calculated field for popularity.”

Give me:
- Exact field name
- Exact formula
- Where to place it
- What aggregation should be used
- What result I should expect

---

# STEP 11 — USE MY LAB MANUAL INTELLIGENTLY

Compare the proposed project to the techniques in my attached Advanced Dashboard Lab Manual.

Identify which techniques we should use from:

- Executive KPI / BAN cards
- Dynamic parameters
- Geographic analysis
- Box-and-whisker plots
- Bullet graphs
- FIXED LOD expressions
- Sets
- Set actions
- Waterfall charts
- Forecasting
- Top-N sets
- Parameter actions
- Dashboard navigation
- Story
- Device layouts

For each technique, tell me:

### “Use”
or
### “Do not use”

and explain why.

The project should feel advanced but not artificially overloaded.

---

# STEP 12 — DASHBOARD UX/UI DESIGN

Design the visual appearance professionally.

Recommend:
- Dashboard dimensions
- Layout
- Containers
- Spacing
- Font hierarchy
- Background
- KPI card design
- Chart placement
- Filter placement
- Tooltip structure
- Color logic
- Titles
- Navigation buttons

Keep the visual style:
### Modern + analytical + professional + clean

Avoid:
- excessive colors
- unnecessary pie charts
- 3D charts
- clutter
- decorative visuals with no analytical purpose

Use a consistent visual language across all three dashboards.

---

# STEP 13 — USER FLOW

The dashboard should tell a story:

### PAGE 1
“What does the restaurant ecosystem look like?”

↓

### PAGE 2
“Why is restaurant selection difficult and what patterns exist?”

↓

### PAGE 3
“How can our proposed ranking framework solve the problem?”

Create navigation buttons such as:

Overview → Segmentation → Recommendation Simulator

and:

Home → Previous → Next

Explain exactly how to create these in Tableau.

---

# STEP 14 — BUSINESS INSIGHTS

After the dashboard is built, help me extract genuine findings.

For each finding, provide:

### Finding
What does the data show?

### Evidence
Which visualization demonstrates it?

### Business Meaning
Why does it matter?

### Recommendation
What should Zomato do?

Never fabricate findings before analyzing the actual dataset.

---

# STEP 15 — FINAL BUSINESS RECOMMENDATIONS

Produce 4–6 actionable recommendations.

Every recommendation must have:

Problem
→ Evidence
→ Action
→ Expected benefit
→ Measurement KPI

Example structure:

“High-rated but low-engagement restaurants can be surfaced more prominently in relevant searches because they appear underrepresented in popularity-based rankings.”

Only make such a recommendation if the data actually supports it.

---

# STEP 16 — LIMITATIONS

Create a strong limitations section.

Be explicit that a public restaurant dataset may not contain:
- individual user browsing history
- clicks
- orders
- delivery times
- cancellation data
- user preferences
- conversion rate
- actual ranking positions
- real-time location
- proprietary Zomato recommendation features

Therefore:

### Do not present the project as Zomato's real recommendation algorithm.

Present it as:

### “A transparent academic prototype inspired by a real restaurant-discovery/ranking problem.”

Explain what additional data would be required to productionize the solution.

---

# STEP 17 — REPORT

After the dashboard design is finalized, help me create the complete written report.

Structure:

1. Title
2. Executive Summary
3. Introduction
4. Company/Industry Background
5. Problem Statement
6. Why the Problem Matters
7. Research / Existing Industry Approach
8. Dataset Description
9. Data Cleaning
10. Exploratory Analysis
11. Methodology
12. Restaurant Relevance Score
13. Tableau Dashboard Design
14. Key Findings
15. Proposed Solution
16. Recommendations
17. Limitations
18. Future Scope
19. Conclusion
20. References

Use simple, natural university-level language.

Do not make the writing sound like AI-generated corporate jargon.

---

# STEP 18 — PRESENTATION

Create a presentation structure of approximately 10–15 slides.

Include:
- Problem
- Why it matters
- Zomato context
- Dataset
- Methodology
- Important visualizations
- Relevance score
- Dashboard
- Findings
- Proposed solution
- Recommendations
- Limitations
- Conclusion

Also give me a concise speaking script for each slide.

---

# STEP 19 — VIVA PREPARATION

Prepare likely questions such as:

- Why did you choose this problem?
- Why Zomato?
- Why is restaurant discovery a business problem?
- Why did you select these variables?
- Why these weights?
- Why normalize the variables?
- Why use an LOD?
- Why use a parameter?
- Why use a set?
- Why use Tableau instead of Python?
- How is this different from a simple Top-N filter?
- How do you know the ranking works?
- What are the limitations?
- Can this be deployed by Zomato?
- What additional data would be required?
- How could machine learning improve it?

Give simple but technically correct answers.

---

# VERY IMPORTANT RULES

1. NEVER fabricate data.
2. NEVER assume a dataset column exists before checking.
3. NEVER invent Zomato internal metrics.
4. NEVER claim our prototype is Zomato's actual production algorithm.
5. Separate facts, inference, and our proposed methodology.
6. Use reliable citations for external research.
7. Use the attached lab manual as the technical reference.
8. Prefer exact Tableau instructions over generic explanations.
9. Keep the project advanced but realistically buildable by a student.
10. Avoid unnecessary charts.
11. Every visualization must have a business purpose.
12. Every major insight must connect back to the original problem.
13. The final dashboard must clearly demonstrate a SOLUTION, not just analysis.
14. If the dataset is not suitable for a component of the proposed solution, tell me and redesign that component instead of forcing it.
15. Do not move to the next major stage until the current stage is logically validated.

---

# HOW I WANT YOU TO WORK WITH ME

Work sequentially.

Start ONLY with:

### PHASE 1 — DATASET & PROBLEM VALIDATION

First inspect the attached dataset and give me:

1. Dataset summary
2. Column-by-column assessment
3. Data-quality issues
4. Variables relevant to restaurant ranking
5. Variables that should NOT be used and why
6. Whether the proposed problem is defensible
7. Recommended final problem statement
8. Recommended final project title
9. Recommended stakeholders
10. Recommended analytical approach
11. Any changes you recommend to make the case stronger

Do NOT jump into creating all the dashboards immediately.

Once Phase 1 is complete, wait for me to continue.

When I say **“START PHASE 2”**, move to the next stage.

Continue this structured workflow until the entire Tableau project is complete.