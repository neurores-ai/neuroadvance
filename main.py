import streamlit as st
from PIL import Image
st.set_page_config(page_title='Neuroadvance consulting',layout='wide')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
local_css('style/style.css')

st.title('Neuroadvance consulting')
st.subheader('Investigación médica en Estados Unidos')
st.caption('Todo lo que debes saber para acceder a estadías de investigación/ observación neuroquirúrigca en Estados Unidos ')


with st.container():
    st.write('---')
    left_column,right_column=st.columns(2)
    file3=Image.open('foto_perfil.png')
    with right_column:
        st.header('Quienes somos?')
        st.write('##')
        st.write(
            """
            Somos una empresa formada por exitosos profesionales de la salud que han realizado estadias de perfeccionamiento en Estados Unidos.
             La empresa nace  de la experiencia del Dr. Nicolás González Romo, neurocirujano chileno, quien ha realizado estudios de perfeccionamiento en prestigiosos centros clínicos tales como St. Louis University Hospital (St.Louis,MO), Weill Cornell Medical College (NYC, NY) 
            y Barrow Neurological Instiute (PHX,AZ).
            
            """
        )
    with left_column:
        st.image(file3,caption='Dr.Nicolás González Romo',width=300)

with st.container():
    st.write('---')
    left_column,right_column=st.columns(2)
    file=Image.open('neurplex.jpeg')
    with left_column:
        st.header('Ventajas de realizar investigación en USA')
        st.write('##')
        st.write(
            """
            Obtén accesso a los mejores centros clínicos de investigación 
            - Crea valiosos contactos profesionales
            - Realiza publicaciones científicas
            - Mejora tu nivel inglés
            - Accede a cursos de perfeccionamiento 
            - Accede a los mejores congresos científicos
            - Potencia tu curriculum vitae (CV)  
            - Planea una estrategia profesional 
            - Posibilidad de obtener remuneración
            """
        )
    with right_column:
        st.image(file,caption='Barrow Neurological Institute')
with st.container():
     st.write('---')
     left_column, right_column = st.columns(2)
     file2=Image.open('doctor.png')
     with right_column:
         st.header('Nuestros servicios')
         st.write('##')
         st.write(
             """
             Asesoría completa y personalizada: 
             - Postulación 
             - Carta de recomendación
             - Cuáles son las mejores visas para realizar investigación en Estados Unidos
             - La mejor estrategia para obtener alojamiento prolongado 6- 12 meses
             - Cómo abrir una cuenta bancaria
             - Como obtener licencia de conducir
             - Pasos para convalidar título médico a través de ECFMG
             - Recomendaciones para el grupo familiar 
             """
         )
         st.write(
             """
             Consultoría modalidad Zoom 
             - Entrevista personalizada (45 minutos) 
             - valor: 500 USD
             """
         )
     with left_column:
         st.image(file2)
with st.container():
    st.write('---')
    st.header('Contacto')
    st.write('##')
    contact_form= """
    <form action="https://formsubmit.co/ngr@neurores.ai" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre aquí" required>
        <input type="email" name="email" placeholder="Tu correo aquí" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
with st.container():
    st.write('---')
    st.write('Neuroadvance consulting, todos los derechos reservados')

