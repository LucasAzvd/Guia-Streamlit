  
import streamlit as st
import pandas as pd

def main():
    st.title("Hello World!!")
    numero1 = 1
    st.markdown(f'# {numero1} Coloquei uma variável aq')
    
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.text("This is a text")
    #st.image('logo.png')
    #st.audio('record.wav')
    #st.video('asadssda.mp4')

    # Botão
    botao = st.button('Botao')
    if botao:
        st.text('clicado')

    # Check Box
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Checado')

    # Seletor de opção
    radio = st.radio('Escolhas as opções',('Opt 1', 'Opt 2'))
    if radio == 'Opt 1':
        st.markdown('Opt 1')
    if radio == 'Opt 2':
        st.markdown('Opt 2')

    # Select Box
    select = st.selectbox("Escolha:", ('Opt 1', 'Opt 2'))
    if select == 'Opt 1':
        st.markdown('Opt 1')
    if select == 'Opt 2':
        st.markdown('Opt 2')

    # Select multiplo
    multi = st.multiselect('Escolha', ('Opt 1', 'Opt 2'))
    if multi == 'Opt 1':
        st.markdown('Opt 1')
    if multi == 'Opt 1':
        st.markdown('Opt 2')
    
    # Upload de arquivos
    file = st.file_uploader('Escolha seu arquivo', type='csv')
    if file is not None:
        number = st.slider('Escolha o numero de linhas que deseja ver', min_value=1, max_value=20)
        df = pd.read_csv(file)
        st.dataframe(df.head(number))

if __name__ == '__main__':
    main()