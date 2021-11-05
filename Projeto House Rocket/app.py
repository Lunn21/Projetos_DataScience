import joblib
import streamlit as st
 
# loading the trained model

classifier = joblib.load('D:\Arquivos\Documents\MeusProjetos\Projetos_DataScience\Projeto House Rocket\model2.pkl')
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement,yr_built, yr_renovated, zipcode, lat, longi, sqft_living15, sqft_lot15):   

    # Making predictions 
    prediction = classifier.predict( 
        [[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement,yr_built, yr_renovated, zipcode, lat, longi, sqft_living15, sqft_lot15]])
    
    return prediction
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Previsão de Preço Imobiliario</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    bedrooms = st.number_input("Quartos")
    bathrooms = st.number_input("Banheiros") 
    sqft_living = st.number_input("Metros quadrados da construção") 
    sqft_lot = st.number_input("Metros quadrados do terreno") 
    floors = st.number_input("Andares") 
    waterfront = st.number_input("Água na frente") 
    view = st.number_input("Vista") 
    condition = st.number_input("Condição") 
    grade = st.number_input("Grau") 
    sqft_above = st.number_input("Metros quadrados do segundo andar") 
    sqft_basement = st.number_input("Metros quadrados do porão") 
    yr_built = st.number_input("Ano de construção") 
    yr_renovated = st.number_input("Ano de Renovação") 
    zipcode = st.number_input("Codigo Postal") 
    lat = st.number_input("Latitude") 
    longi = st.number_input("Longitude") 
    sqft_living15 = st.number_input("Metros quadrados para vizinho") 
    sqft_lot15 = st.number_input("Metros quadrados para terreno vizinho") 
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement,yr_built, yr_renovated, zipcode, lat, longi, sqft_living15, sqft_lot15) 
        st.success('O Preço avaliado é {}'.format(result))
     
if __name__=='__main__': 
    main()