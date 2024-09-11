import streamlit as st
import pandas as pd

# import plotly.express as px

TITLE = "Graphing from a Spreadsheet"


@st.cache_data
def load_data():
    return pd.read_csv("gameconsoles.csv")


st.set_page_config(page_title=TITLE, page_icon=":bar_chart:", layout="wide")

st.title(TITLE)

st.write(
    "This is a simple Streamlit app that reads a spreadsheet and graphs the data. (or at least it will be)"
)
st.write("At the moment all it does is show the data from the spreadsheet")
# This gets called so that the data can be cached, rather than reloaded every time
df = load_data()
st.dataframe(df)


# Create a bar chart based on this data
# print(df.columns)
st.bar_chart(
    df, x="Company", y="Units sold (million)", use_container_width=True, height=400
)

print(df["Released Year"].min(), df["Released Year"].max())
df["Discontinuation Year"] = df["Discontinuation Year"].replace(0, 2024)
df["Discontinuation Year"] = df["Discontinuation Year"].fillna(
    df["Discontinuation Year"].max()
)

st.vega_lite_chart(
    df,
    {
        "mark": {"type": "circle", "tooltip": {"content": "data"}, "size": 400},
        "encoding": {
            "x": {
                "field": "Released Year",
                "type": "quantitative",
                "scale": {"domainMin": 1970, "domainMax": 2025},
            },
            "y": {"field": "Units sold (million)", "type": "quantitative"},
            "color": {"field": "Console Name", "type": "nominal"},
        },
    },
    height=600,
    theme=None,
    use_container_width=True,
)


st.sidebar.success("Select a page from the list above")
