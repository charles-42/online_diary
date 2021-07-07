import sys
sys.path.insert(0, "/Users/charles/github/online_diary")
import streamlit as st
import requests
from datetime import datetime, date
from mysql.connector.errors import IntegrityError
from src.utils.functions import *
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

#Create the header and the menu panel
d = date.today()

menu = st.sidebar.radio("Que souhaitez-vous faire ?", ("Ajouter un nouveau texte", "Modifier un texte", "Consulter un texte","Supprimer un texte"))

st.header("Votre journal intime en ligne")
st.subheader("Aujourd'hui, nous sommes le {0:%d} {0:%B} {0:%Y}.".format(d))

# each part of the menu correspond to one crud operation
if menu == "Ajouter un nouveau texte":

    #define the url of the API and the path of the collection we work with
    url = 'http://127.0.0.1:8081/text'

    #Define the object attributs we want to send to the API
    user_data = {}
    user_data['text_content'] = st.text_input("Veuillez renseigner votre texte")

    user_data['text_date'] = st.date_input("Veuillez renseigner la date correspondante à votre texte",value = None, min_value = date(1900, 1, 1))
    user_data['text_date'] = str(user_data['text_date'])

    submit_button = st.button("Soumettre")


    if submit_button:
        try :
            #call the API with the post operation
            response = requests.post(url, json = user_data)
            #validation message if everything is alright
            if response.status_code==200:
                st.write("Votre texte : {}".format(user_data['text_content']))
                st.write("Date d'entrée du texte : {}".format(user_data['text_date']))
            #otherwise show the error which occured
            else:
                st.write("une erreur est survenue")
                st.write("Error:",response.status_code,response.text )

        except IntegrityError :
            st.write("Nous n\'avons pas pu vous enregistrer car vous existez déjà dans la base de données")
        except requests.ConnectionError as error:
            print(error)


elif menu == "Modifier un texte":
    #define the url of the API and the path of the collection we work with
    url = 'http://127.0.0.1:8081/text'

    #Define the object attributs we want to send to the API
    user_data = {}
    user_data['text_content'] = st.text_input("Veuillez renseigner votre nouveau texte")

    user_data['text_date'] = st.date_input("Veuillez renseigner la date correspondante à votre texte modifié",value = None, min_value = date(1900, 1, 1))
    user_data['text_date'] = str(user_data['text_date'])

    submit_button = st.button("Soumettre")

    if submit_button:
        try :
            response = requests.put(url, json = user_data)
            #validation message if everything is alright
            if response.status_code==200:
                st.write("Votre texte : {}".format(user_data['text_content']))
                st.write("Date d'entrée du texte : {}".format(user_data['text_date']))
            #otherwise show the error which occured
            else:
                st.write("une erreur est survenue")
                st.write("Error:",response.status_code,response.text)
        except requests.ConnectionError as error:
            print(error)

elif menu == "Consulter un texte":
    #define the url of the API and the path of the collection we work with
    url = 'http://127.0.0.1:8081/text'

    #Define the object attributs we want to send to the API
    user_data = {}
    user_data['text_date'] = st.date_input("De quelle date voulez-vous consulter le texte?",value = None, min_value = date(1900, 1, 1))
    user_data['text_date'] = str(user_data['text_date'])

    submit_button = st.button("Soumettre")

    if submit_button:
        try :
            response = requests.get(url, json = user_data)
            #validation message if everything is alright
            if response.status_code==200:
                try:
                    # The API result is inside the "json" attribut
                    st.write("'",response.json()[0][0],"'")
                except IndexError:
                    st.write("Il n'y a pas de texte enregistré à cette date")
            #otherwise show the error which occured
            else:
                st.write("une erreur est survenue, le texte n'a pas pu être supprimé")
                st.write("Error:",response.status_code)
                st.write("'",response.text,"")
        except requests.ConnectionError as error:
            print(error)

elif menu == "Supprimer un texte":
    #define the url of the API and the path of the collection we work with
    url = 'http://127.0.0.1:8081/text'

    #Define the object attributs we want to send to the API
    user_data = {}
    user_data['text_date'] = st.date_input("De quelle date voulez-vous supprimer le texte?",value = None, min_value = date(1900, 1, 1))
    user_data['text_date'] = str(user_data['text_date'])

    submit_button = st.button("Soumettre")

    if submit_button:
        try :
            response = requests.delete(url, json = user_data)
            #validation message if everything is alright
            if response.status_code==200:
                st.write("Votre texte est bien supprimé")
            #otherwise show the error which occured
            else:
                st.write("une erreur est survenue, le texte n'a pas pu être supprimé")
                st.write("Error:",response.status_code,response.text )
        except requests.ConnectionError as error:
            print(error)
