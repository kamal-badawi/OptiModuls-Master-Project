# Wichtiger Hinweis: Die Übersetzungen wurden mit ChatGPT erstellt
import streamlit as st
from streamlit_navigation_bar import st_navbar
import Feedback_and_Recommendation
import Predictions_Root
import Terms_of_Use
import Predictions_Jobs_Showing

translations_main = {
    0: ["Please confirm that you accept the terms and conditions.",
        "Bitte bestätigen Sie, dass Sie die Bedingungen und Konditionen akzeptieren.",
        "Si prega di confermare di accettare i termini e le condizioni.",
        "Veuillez confirmer que vous acceptez les termes et conditions.",
        "Confirme que acepta los términos y condiciones.", "Por favor, confirme que aceita os termos e condições.",
        "Vänligen bekräfta att du accepterar villkoren.", "Vennligst bekreft at du godtar vilkårene.",
        "Bekræft venligst, at du accepterer betingelserne.", "Proszę potwierdzić, że akceptujesz warunki.",
        "Пожалуйста, подтвердите, что вы принимаете условия.", "Будь ласка, підтвердіть, що ви приймаєте умови."],
    1: ["Language", "Sprache", "Lingua", "Langue", "Idioma", "Idioma", "Språk", "Språk", "Sprog", "Język", "Язык",
        "Мова"],
    2: ["Terms of Use", "Nutzungsbedingungen", "Termini di utilizzo", "Conditions d'utilisation", "Términos de uso", "Termos de uso", "Användarvillkor", "Bruksvilkår", "Brugsvilkår", "Warunki użytkowania", "Условия использования", "Умови використання"],
    3: ["Predictions", "Vorhersagen", "Predizioni", "Prédictions", "Predicciones", "Previsões", "Prognoser", "Prognoser", "Forudsigelser", "Prognozy", "Прогнозы", "Прогнози"],
    4: ["Feedback and Recommendation", "Feedback und Weiterempfehlung", "Feedback e Raccomandazione", "Retour d'information et Recommandation", "Comentarios y Recomendaciones", "Comentários e Recomendações", "Återkoppling och Rekommendation", "Tilbakemelding og Anbefaling", "Feedback og Anbefaling", "Opinie i Rekomendacja", "Обратная связь и Рекомендация", "Зворотний зв'язок та Рекомендація"],

}


# Mache die Seite so breit wie möglich
st.set_page_config(page_title="OptiModuls (Student)", layout="wide")

st.markdown(
    """
    <style>
    /*Side bar*/
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 100%;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 350px;
        margin-left: -400px;
    }

    """,
    unsafe_allow_html=True,
)


if 'language_index' not in st.session_state:
    st.session_state.language_index = 0

language_index = st.session_state.language_index

if 'language_value' not in st.session_state:
    st.session_state.language_value = 'English'

language_value = st.session_state.language_value


if 'top_nav_value' not in st.session_state:
    st.session_state.top_nav_value = translations_main.get(2)[language_index]

top_nav_value = st.session_state.top_nav_value

# Mach die Frabge von allen Text schwarz
# Define the CSS style for text color
st.markdown("""
    <style>
    /* Change text color of all elements */
    * {
        



    }
    </style>
    """, unsafe_allow_html=True)

# Side bar link Styling
st.markdown("""
    <style>
    .st-emotion-cache-6qob1r {
    background-color: #f3f5e9 !important;
    }   
    </style>
    """, unsafe_allow_html=True)

styles = {
    "nav": {
        "background-color": "#f3f5e9",
        "height": "3.25rem",

    },
    "div": {
        "max-width": "85.25rem",
        "font-size": "20px",
        "font-size": "20px",
        "padding": "1rem",

    },
    "span": {
        "color": "var(--text-color)",
        "border-radius": "0.3rem",
        "padding": "1rem",

    },
    "active": {
        "background-color": "#f7e48f",
        "padding": "1rem"
    },
    "hover": {
        "background-color": "#D3D3D3",
    },
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

pages = [
        f'{translations_main.get(2)[language_index]}',
        f'{translations_main.get(3)[language_index]}',
        f'{translations_main.get(4)[language_index]}'
         ]


# navigation_bar_top


# Suche den Index des ausgewählten Begriffs in den Übersetzungen
def return_selected_page_translated(selected_term, target_language_index):
    for key, value in translations_main.items():
        if selected_term in value:
            return value[target_language_index]


selected_page_transalted = return_selected_page_translated(top_nav_value, language_index)

navigation_bar_top = st_navbar(pages=pages,
                               styles=styles,
                               options=options,
                               selected=selected_page_transalted)

############

# berechne die Index der ausgewählten Sprache
language_dict = {
    'English': 0,
    'Deutsch': 1,
    'Italiano': 2,
    'Français': 3,
    'Español': 4,
    'Português': 5,
    'Svenska': 6,
    'Norsk': 7,
    'Dansk': 8,
    'Polski': 9,
    'Русский': 10,
    'українська': 11

}

# Deine Styles hier
options = list(language_dict.keys())



# Navigationsleiste erstellen
logo_column, text_language_column, drop_down_language_column= st.columns([12.5,1,1.4])
with logo_column:
    if str(navigation_bar_top) != f'{translations_main.get(2)[language_index]}':

        # Logo
        hover_style = """
            <style>
            .logo {
                transition: opacity 0.8s ease;
                animation: skalieren 1s infinite linear;
            }
            @keyframes skalieren {
                    0% {
            transform: scale(1, 1);
          }
          50% {
            transform: scale(1.1, 1.1);
          }
          100% {
            transform: scale(1, 1);
          }
            }
    
            </style>
        """

        # Apply the custom CSS
        st.markdown(hover_style, unsafe_allow_html=True)

        st.markdown(
            '<div style="text-align: left;"><img src="https://i.postimg.cc/ZqC6rYvH/Opti-Moduls-Project-QR-Code.png" class="logo" width="100"></div>',
            unsafe_allow_html=True
        )
    else:
        pass

with text_language_column:
    st.write('')
    st.write('')
    st.write(f'**{translations_main.get(1)[language_index]}:** ')

with drop_down_language_column:
    selected_language = st.selectbox('',
                                     options=options)



# Session State überprüfen und neu laden
if 'language_index' not in st.session_state:
    st.session_state.language_index = language_dict.get(selected_language)

if st.session_state.language_index != language_dict.get(selected_language):
    st.session_state.language_index = language_dict.get(selected_language)
    st.experimental_rerun()


# Session State überprüfen und neu laden
if 'language_value' not in st.session_state:
    st.session_state.language_value = selected_language

if st.session_state.language_value != selected_language:
    st.session_state.language_value = selected_language
    st.experimental_rerun()

# Session State überprüfen und neu laden
if 'top_nav_value' not in st.session_state:
    st.session_state.top_nav_value = str(navigation_bar_top)

if st.session_state.top_nav_value != str(navigation_bar_top):
    st.session_state.top_nav_value = str(navigation_bar_top)
    st.experimental_rerun()





############



#Wenn es nicht akzeptiert wurde, zeige die Warnung
#Bei Terms of Use zeige es nicht
#get the Agreemen-Value from Terms of Use checkbox
if 'agree' not in st.session_state:
    agree = False
else:
    agree =  st.session_state.agree


if not agree and str(navigation_bar_top) != f'{translations_main.get(2)[language_index]}':
    for i in range(50):
        st.write('')

    st.warning(f'{translations_main.get(0)[language_index]}')

else:
    # "Terms of Use"
    if navigation_bar_top == f'{translations_main.get(2)[language_index]}':
        Terms_of_Use.run_terms_of_use(language_index)


    # "Predictions"
    if navigation_bar_top == f'{translations_main.get(3)[language_index]}':
        Predictions_Root.run_predictions_root(language_index,
                                              f'{translations_main.get(3)[language_index]}')


    # "Feedback and Recommendation"
    if navigation_bar_top == f'{translations_main.get(4)[language_index]}':
        Feedback_and_Recommendation.run_feedback_and_recommendation(language_index,
                                                                    f'{translations_main.get(4)[language_index]}')

