import dash_mantine_components as dmc
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from dash import _dash_renderer
_dash_renderer._set_react_version("18.2.0")

# Sample data for graphs
df = px.data.gapminder().query("year == 2007")

# Initialize the app
app = Dash(external_stylesheets=dmc.styles.ALL)

# Header with ALS Logo and title
header = dmc.Group(
    [
        dmc.Image(src=app.get_asset_url("als_logo_wheel.png"), w=40, h=40),  # Logo image
        dmc.Text("My ALS Dash App", 
                 fw=700, 
                 c="sky.9",
                 style={"font-size": "2rem"}
        )  # App title
    ],
    align="center",
    justify="center",
    h="100%"
)
sidebarInputSection = dmc.Stack(
    [
        dmc.NumberInput(
            label="Example Input",
            description="Description",
            value=5,
            min=0,
            step=5,
            w=250,
        ),
        dmc.NumberInput(
            label="Example Input",
            description="Description",
            value=0,
            min=0,
            step=5,
            w=250,
        ),
        dmc.RadioGroup(
            children=dmc.Group(
                [dmc.Radio(i, value=i) for i in ["USA", "Canada", "France"]], my=10
            ),
            value="USA",
            label="Size Example - small",
            size="sm",
            mt=10,
        ),
    ],
    align="left",
    h="100%",
    ps="1rem"
)

sidebarGroup1 = dmc.Stack(
    children=[
        dmc.Text("Section Title", fw=700, size="lg", c="sky.8"),
        sidebarInputSection,
    ],
    align="left",
)

sidebarGroup2 = dmc.Stack(
    children=[
        dmc.Text("Section Title", fw=700, size="lg", c="sky.8"),
        sidebarInputSection,
    ],
    align="left",
)

# Sidebar simulation with dmc.Stack for vertical stacking
sidebar = dmc.Stack(
    children=[
        sidebarGroup1,
        sidebarGroup2
    ],
    align="left",
    bg="slate.2",
    h="100%",
    p="1rem",
    gap="3rem"
)



# Main content area with sample widgets
main_content = dmc.Box(
    [
        dmc.SimpleGrid(
            cols=2,
            children=[
                dmc.Card(
                    dcc.Graph(
                        figure=px.scatter(df, x="gdpPercap", y="lifeExp", title="Life Expectancy vs GDP")
                    ),
                    padding="lg", shadow="dark"
                ),
                dmc.Card(
                     dcc.Graph(
                        figure=px.bar(df, x="continent", y="pop", title="Population by Continent")
                    ),
                    padding="lg", shadow="dark"
                )
            ]
        ),
        dmc.Card(
                    dcc.Graph(
                        figure=px.bar(df, x="continent", y="pop", title="Population by Continent")
                    ),
                    padding="lg", shadow="dark", mt="1rem"
                )
    ],
    bg="slate.5",
    h="100%",
    p="1rem",
    style={"overflow":"auto"}
)



# App layout using dmc.Group to horizontally align sidebar and main content
app.layout = dmc.MantineProvider(
    theme={
    "colors": {
        "sky": [                
            "rgb(240 249 255)",
            "rgb(224 242 254)",
            "rgb(186 230 253)",
            "rgb(125 211 252)",
            "rgb(56 189 248)",
            "rgb(14 165 233)",
            "rgb(2 132 199)",
            "rgb(3 105 161)",
            "rgb(7 89 133)",
            "rgb(12 74 110)",                
        ],
        "slate": [
            "rgb(248 250 252)",
            "rgb(241 245 249)",
            "rgb(226 232 240)",
            "rgb(203 213 225)",
            "rgb(148 163 184)",
            "rgb(100 116 139)",
            "rgb(71 85 105)",
            "rgb(51 65 85)",
            "rgb(30 41 59)",
            "rgb(15 23 42)"
        ]
    },
    "shadows": {"dark": "3px 4px 8px rgb(51 65 85)"},
    },
    children=[
        dmc.AppShell(
            [
                #dcc.Store
                dmc.AppShellHeader(children=[header], zIndex=3000),
                dmc.AppShellNavbar(children=[sidebar], style={"box-shadow":"3px 0px 8px rgb(15 23 42)"}),
                dmc.AppShellMain(children=[main_content], style={"height":"100%"})
            ],
            header={"height": 70},
            navbar={
                "width": 300,
                "breakpoint": "sm",
            },
            style={
                "height": "100vh"
            }
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
