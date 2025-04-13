def get_theme_css(st):
    primary_text = st.get_option("theme.textColor") or "#000"
    secondary_text = "#888" if primary_text == "#000" else "#ccc"
    background_card = "#f7f7f7" if primary_text == "#000" else "#111"
    css = f'''
        <style>
            h1, h2, h3, h4, p, span, div {{
                color: {primary_text};
            }}
            .secondary-text {{
                color: {secondary_text};
            }}
        </style>
    '''
    return primary_text, secondary_text, background_card, css