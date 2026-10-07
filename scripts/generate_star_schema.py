"""
Generate High-Resolution, Publication-Grade Star Schema Diagram for Zomato Business Intelligence Case Study
CIA IIIB Assessment: Data Warehousing, ETL, Dimensional Modeling & OLAP
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_star_schema():
    # Setup canvas
    fig, ax = plt.subplots(figsize=(20, 14.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#F8FAFC')

    # Color Palette
    c_fact_header = '#1E293B'      # Slate 800
    c_fact_body = '#F1F5F9'        # Slate 100
    c_dim_header = '#0284C7'       # Light blue 600
    c_dim_body = '#F0F9FF'         # Sky 50
    c_border = '#0F172A'
    c_text = '#0F172A'
    c_pk = '#DC2626'              # Red 600
    c_fk = '#2563EB'              # Blue 600

    def draw_table(x, y, w, h, title, pk_list, fk_list, attr_list, is_fact=False):
        h_color = c_fact_header if is_fact else c_dim_header
        b_color = c_fact_body if is_fact else c_dim_body
        
        # Shadow
        shadow = patches.FancyBboxPatch((x+0.08, y-h-0.08), w, h, boxstyle="round,pad=0.03,rounding_size=0.12",
                                        facecolor='#CBD5E1', edgecolor='none', zorder=1)
        ax.add_patch(shadow)

        # Body container
        box = patches.FancyBboxPatch((x, y-h), w, h, boxstyle="round,pad=0.03,rounding_size=0.12",
                                     facecolor=b_color, edgecolor=c_border, linewidth=1.8, zorder=2)
        ax.add_patch(box)

        # Header box
        head_h = 0.85
        header_box = patches.FancyBboxPatch((x, y-head_h), w, head_h, boxstyle="round,pad=0.03,rounding_size=0.12",
                                            facecolor=h_color, edgecolor=c_border, linewidth=1.8, zorder=3)
        ax.add_patch(header_box)
        
        # Title text
        tag = "[FACT TABLE]" if is_fact else "[DIMENSION TABLE]"
        ax.text(x + w/2, y - 0.32, title, ha='center', va='center', fontsize=11.5, fontweight='bold', color='white', zorder=4)
        ax.text(x + w/2, y - 0.65, tag, ha='center', va='center', fontsize=8.5, fontweight='bold', 
                color='#38BDF8' if not is_fact else '#FDA4AF', zorder=4)

        # Content lines
        curr_y = y - head_h - 0.32
        line_spacing = 0.30

        # PK
        for pk in pk_list:
            ax.text(x + 0.20, curr_y, "PK", fontsize=8.5, fontweight='bold', color=c_pk, zorder=4)
            ax.text(x + 0.75, curr_y, pk, fontsize=9.0, fontweight='bold', color=c_text, zorder=4)
            curr_y -= line_spacing

        # FK
        for fk in fk_list:
            ax.text(x + 0.20, curr_y, "FK", fontsize=8.5, fontweight='bold', color=c_fk, zorder=4)
            ax.text(x + 0.75, curr_y, fk, fontsize=9.0, fontweight='bold', color=c_text, zorder=4)
            curr_y -= line_spacing

        # Attributes
        for attr in attr_list:
            ax.text(x + 0.75, curr_y, attr, fontsize=8.8, color='#334155', zorder=4)
            curr_y -= line_spacing

    # ==========================
    # 1. CENTRAL FACT TABLE
    # ==========================
    fact_x, fact_y, fact_w, fact_h = 7.6, 10.4, 4.8, 6.7
    fact_pks = ["Fact_Listing_Key (BIGINT)"]
    fact_fks = [
        "Restaurant_Key (INT)",
        "Location_Key (INT)",
        "Cuisine_Key (INT)",
        "Service_Key (INT)",
        "Price_Tier_Key (INT)",
        "Segment_Key (INT)"
    ]
    fact_measures = [
        "Aggregate_Rating (DECIMAL 2,1)",
        "Votes (INT - Review Volume)",
        "Log_Votes (FLOAT - Scaled Social Proof)",
        "Average_Cost_Clean (DECIMAL 10,2)",
        "Normalized_Rating_Score (FLOAT 0-100)",
        "Normalized_Engagement_Score (FLOAT 0-100)",
        "Budget_Fit_Score (FLOAT 0-100)",
        "Relevance_Score (FLOAT 0-100)",
        "Is_Rated_Flag (TINYINT 0/1)",
        "Listing_Count (INT = 1)"
    ]
    draw_table(fact_x, fact_y, fact_w, fact_h, "FACT_RESTAURANT_PERFORMANCE", fact_pks, fact_fks, fact_measures, is_fact=True)

    # ==========================
    # 2. LEFT DIMENSIONS
    # ==========================
    # Dim Restaurant (Top Left)
    r_x, r_y, r_w, r_h = 1.2, 13.0, 4.4, 3.2
    draw_table(r_x, r_y, r_w, r_h, "DIM_RESTAURANT", ["Restaurant_Key (INT)"], [], [
        "Restaurant_ID (NATURAL KEY)",
        "Restaurant_Name (VARCHAR 150)",
        "Address (VARCHAR 255)",
        "Is_Chain_Brand (BOOLEAN)",
        "Outlet_Count_In_City (INT)"
    ])

    # Dim Cuisine (Middle Left)
    c_x, c_y, c_w, c_h = 1.2, 8.9, 4.4, 3.2
    draw_table(c_x, c_y, c_w, c_h, "DIM_CUISINE", ["Cuisine_Key (INT)"], [], [
        "Primary_Cuisine (VARCHAR 80)",
        "Cuisine_Category (VARCHAR 50)",
        "Cuisine_Count (INT)",
        "Full_Cuisine_List (VARCHAR 255)",
        "Is_Multi_Cuisine (BOOLEAN)"
    ])

    # Dim Price Tier (Bottom Left)
    p_x, p_y, p_w, p_h = 1.2, 4.8, 4.4, 3.2
    draw_table(p_x, p_y, p_w, p_h, "DIM_PRICE_TIER", ["Price_Tier_Key (INT)"], [], [
        "Price_Range (INT 1-4)",
        "Price_Tier_Name (VARCHAR 50)",
        "Currency_Code (VARCHAR 10)",
        "Budget_Classification (VARCHAR 30)",
        "Benchmark_Avg_Cost (DECIMAL)"
    ])

    # ==========================
    # 3. RIGHT DIMENSIONS
    # ==========================
    # Dim Location (Top Right)
    l_x, l_y, l_w, l_h = 14.4, 13.0, 4.4, 3.8
    draw_table(l_x, l_y, l_w, l_h, "DIM_LOCATION", ["Location_Key (INT)"], [], [
        "Locality (VARCHAR 100)",
        "Locality_Verbose (VARCHAR 150)",
        "City (VARCHAR 80)",
        "Country_Code (INT)",
        "Country_Name (VARCHAR 60)",
        "Latitude (FLOAT)",
        "Longitude (FLOAT)",
        "Has_Valid_Coordinates (BOOLEAN)"
    ])

    # Dim Service Profile (Middle Right)
    s_x, s_y, s_w, s_h = 14.4, 8.4, 4.4, 3.2
    draw_table(s_x, s_y, s_w, s_h, "DIM_SERVICE_PROFILE", ["Service_Key (INT)"], [], [
        "Has_Online_Delivery (VARCHAR 5)",
        "Has_Table_Booking (VARCHAR 5)",
        "Is_Delivering_Now (VARCHAR 5)",
        "Service_Profile_Name (VARCHAR 50)",
        "Service_Readiness_Score (FLOAT)"
    ])

    # Dim Restaurant Segment (Bottom Right)
    seg_x, seg_y, seg_w, seg_h = 14.4, 4.4, 4.4, 3.2
    draw_table(seg_x, seg_y, seg_w, seg_h, "DIM_RESTAURANT_SEGMENT", ["Segment_Key (INT)"], [], [
        "Restaurant_Segment (VARCHAR 50)",
        "Rating_Status (Rated/Unrated)",
        "Rating_Text (Excellent/Good/etc)",
        "Rating_Color_Code (VARCHAR 30)",
        "Strategic_Action (VARCHAR 80)"
    ])

    # ==========================
    # 4. RELATIONSHIP CONNECTORS
    # ==========================
    def draw_connector(start_pt, end_pt, label="1 : N", rad=0.0):
        ax.annotate('', xy=end_pt, xytext=start_pt,
                    arrowprops=dict(arrowstyle="-|>", color="#0284C7", lw=2.2, mutation_scale=16,
                                    shrinkA=4, shrinkB=4,
                                    connectionstyle=f"arc3,rad={rad}"))
        mid_x = (start_pt[0] + end_pt[0]) / 2
        mid_y = (start_pt[1] + end_pt[1]) / 2
        ax.text(mid_x, mid_y, label, fontsize=9.0, fontweight='bold', color='#0369A1',
                bbox=dict(boxstyle="round,pad=0.25", facecolor='#FFFFFF', edgecolor='#38BDF8', lw=1.2),
                ha='center', va='center', zorder=6)

    # Left to Center
    draw_connector((r_x + r_w, r_y - r_h/2), (fact_x, fact_y - 1.2), label="1 : N", rad=0.04)
    draw_connector((c_x + c_w, c_y - c_h/2), (fact_x, fact_y - fact_h/2), label="1 : N", rad=0.0)
    draw_connector((p_x + p_w, p_y - p_h/2), (fact_x, fact_y - fact_h + 1.2), label="1 : N", rad=-0.04)

    # Right to Center
    draw_connector((l_x, l_y - l_h/2), (fact_x + fact_w, fact_y - 1.2), label="1 : N", rad=-0.04)
    draw_connector((s_x, s_y - s_h/2), (fact_x + fact_w, fact_y - fact_h/2), label="1 : N", rad=0.0)
    draw_connector((seg_x, seg_y - seg_h/2), (fact_x + fact_w, fact_y - fact_h + 1.2), label="1 : N", rad=0.04)

    # ==========================
    # 5. TITLES & ARCHITECTURAL FOOTER
    # ==========================
    fig.text(0.5, 0.975, "ZOMATO RESTAURANT DISCOVERY & RELEVANCE ANALYTICS",
             ha='center', fontsize=21, fontweight='bold', color='#0F172A')
    fig.text(0.5, 0.950, "Enterprise Dimensional Model (Star Schema) | CIA IIIB Business Intelligence Architecture",
             ha='center', fontsize=12.5, fontweight='semibold', color='#475569')

    # Bottom Architectural Legend Banner
    leg_x, leg_y, leg_w, leg_h = 1.2, 1.25, 17.6, 0.95
    leg_box = patches.FancyBboxPatch((leg_x, leg_y - leg_h), leg_w, leg_h, boxstyle="round,pad=0.03,rounding_size=0.12",
                                    facecolor='#FFFFFF', edgecolor='#94A3B8', linewidth=1.5, zorder=2)
    ax.add_patch(leg_box)
    
    ax.text(1.5, leg_y - 0.28, "ARCHITECTURAL CONFORMANCE (KIMBALL METHODOLOGY & CIA IIIB RUBRIC):", fontsize=9.5, fontweight='bold', color='#1E293B')
    ax.text(1.5, leg_y - 0.55, "[PK] Primary Surrogate Key (Integer Identity)", fontsize=8.5, fontweight='bold', color=c_pk)
    ax.text(1.5, leg_y - 0.78, "[FK] Foreign Key Reference (Relational Integrity)", fontsize=8.5, fontweight='bold', color=c_fk)
    ax.text(7.2, leg_y - 0.55, "* Fact Grain: Exactly 1 record per restaurant outlet profile", fontsize=8.5, color='#334155')
    ax.text(7.2, leg_y - 0.78, "* Additive Facts: Listing_Count, Review Votes, Scaled Cost/Revenue", fontsize=8.5, color='#334155')
    ax.text(13.2, leg_y - 0.55, "* OLAP Slicing: By Price Tier, Cuisine, Delivery Channel", fontsize=8.5, color='#334155')
    ax.text(13.2, leg_y - 0.78, "* OLAP Drill-Down: Country -> City -> Locality Hierarchy", fontsize=8.5, color='#334155')

    ax.set_xlim(0, 20)
    ax.set_ylim(0, 14.5)
    ax.axis('off')

    plt.tight_layout()
    output_path = "Zomato_Star_Schema.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade Star Schema visual saved to: {output_path}")

if __name__ == "__main__":
    draw_star_schema()

