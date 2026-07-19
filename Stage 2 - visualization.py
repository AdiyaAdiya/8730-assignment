
#------------------------------------------------------------------------------
#Visualization 1: Dividend Yield Comparison
#------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.bar(
    competitor_analysis["company"],
    competitor_analysis["dividend_yield_numeric"]*100
)

plt.xticks(rotation=45, ha='right')
plt.ylabel("Dividend Yield (%)")
plt.title("Dividend Yield Comparison among Retail REIT Competitors")

plt.tight_layout()
plt.show()



#-------------------------------------------------------------------------
#Visualization 2: Market Cap + Dividend Yield Combo Chart
#----------------------------------------------------------------------------

import matplotlib.pyplot as plt

companies = competitor_analysis["company"]

market_cap = (
    competitor_analysis["market_cap_numeric"] / 1e9
)

dividend_yield = (
    competitor_analysis["dividend_yield_numeric"] * 100
)

fig, ax1 = plt.subplots(figsize=(11,6))

# BAR CHART
bars = ax1.bar(
    companies,
    market_cap,
    alpha=0.7,
    label="Market Cap"
)

ax1.set_ylabel(
    "Market Capitalization (Billion CAD)"
)

ax1.set_xlabel("Retail REIT Competitors")

plt.xticks(rotation=30, ha="right")


# SECOND AXIS FOR DIVIDEND YIELD
ax2 = ax1.twinx()

ax2.plot(
    companies,
    dividend_yield,
    marker='o',
    linewidth=3,
    label="Dividend Yield (%)"
)

ax2.set_ylabel(
    "Dividend Yield (%)"
)

plt.title(
    "Retail REIT Competitor Comparison:\nMarket Capitalization and Dividend Yield"
)


# Market cap labels
for bar in bars:

    y = bar.get_height()

    ax1.text(
        bar.get_x() + bar.get_width()/2,
        y,
        f"{y:.2f}B",
        ha='center',
        va='bottom'
    )


# Dividend labels
for x, y in zip(companies, dividend_yield):

    ax2.text(
        x,
        y + 0.15,
        f"{y:.2f}%",
        ha='center'
    )


fig.tight_layout()

plt.show()



#------------------------------------------------------------------------------------------
#Visualization 3: Overall Benchmark Ranking
#------------------------------------------------------------------------------------------



competitor_analysis["overall_benchmark_score"] = (
    competitor_analysis["dividend_yield_rank"]
    +
    competitor_analysis["market_cap_rank"]
)

benchmark_df = (
    competitor_analysis
    .sort_values(
        by="overall_benchmark_score",
        ascending=True
    )
)

plt.figure(figsize=(10,6))

bars = plt.barh(
    benchmark_df["company"],
    benchmark_df["overall_benchmark_score"]
)

plt.xlabel(
    "Overall Benchmark Score (Lower = Better)"
)

plt.ylabel(
    "Retail REIT Competitors"
)

plt.title(
    "Overall Retail REIT Benchmark Ranking"
)

plt.gca().invert_yaxis()

for bar in bars:

    width = bar.get_width()

    plt.text(
        width + 0.05,
        bar.get_y() + bar.get_height()/2,
        f"{width:.0f}",
        va='center'
    )

plt.tight_layout()
plt.show()
