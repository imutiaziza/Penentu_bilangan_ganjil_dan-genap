import streamlit as st

# Fungsi untuk menentukan bilangan ganjil atau genap
def check_odd_even(number):
    if number % 2 == 0:
        return "genap"
    else:
        return "ganjil"

# Fungsi utama Streamlit
def main():
    st.title('Penentu Bilangan Ganjil atau Genap')

    # Input bilangan dari pengguna
    number = st.number_input('Masukkan bilangan', step=1)

    # Tombol untuk mengecek bilangan
    if st.button('Cek'):
        result = check_odd_even(number)
        st.success(f'Bilangan {number} adalah bilangan {result}')

if __name__ == "__main__":
    main()





 


















