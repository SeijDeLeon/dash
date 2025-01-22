# Dash App Template
A basic UI template utilizing Dash Mantine in coordination with ALS Computing color styles.
<img width="1659" alt="image" src="https://github.com/user-attachments/assets/186b67f9-ef2d-476f-9819-3095ba3a0b8b" />


# Setup
Install the dependencies and run the app.
```
#Optionally create a new python environment, then install dash and mantine
pip install dash
pip install dash-mantine-components
```

Run the app \
``` python app.py ```
# Using ALS Computing Colors
In `app.py` you will see the following declarations for custom colors <mark>sky</mark> and <mark>slate</mark>

```
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
```

sky and slate are now effectively arrays containing ten shades each, where the larger element has a darker shade. Acceptable values are array indexed, so 0-9. 

The ALS style guide utilizes the Tailwind color system (intended for direct use in React based apps). Dash Mantine can host custom colors, but requires each color to have exactly ten shades. A mapping is made between the Tailwind system and Dash Mantine.
| Tailwind | dash theme |
| --- | --- |
| slate-50 | slate.0 |
| slate-100 | slate.1 |
| slate-200 | slate.2 |
| slate-300 | slate.3 |
| slate-400 | slate.4 |
| slate-500 | slate.5 |
| slate-600 | slate.6 |
| slate-700 | slate.7 |
| slate-800 | slate.8 |
| slate-900 | slate.9 |
|---| --- |
| sky-50 | sky.0 |
| sky-100 | sky.1 |
| sky-200 | sky.2 |
| sky-300 | sky.3 |
| sky-400 | sky.4 |
| sky-500 | sky.5 |
| sky-600 | sky.6 |
| sky-700 | sky.7 |
| sky-800 | sky.8 |
| sky-900 | sky.9 |

These colors can now be used with any dash mantine component that accepts a color property. For example, the background color property of the sidebar component can be set as the third slate shade with `slate.2`

```
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
```
# Best Practices
It is recommended to first draft a basic layout of your app in Figma using the ALS Compute style guide colors, then when creating the app in dash you can directly reference the colors from Figma using this custom color system.
