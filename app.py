# uWu translator using python
import streamlit as st
import generateUwU

def show_output(final_pred):

	st.text("""""")
	st.write(
	"""
	## 🎯 Copy and paste, wherever you want.
	"""
	)

	st.text(final_pred)

	st.write(
	"""
	## 👁️ If you like it try another line. You can also make a donation so that cool projects like these can stay afloat. Donate [here](https://www.iamroyakash.com/donate)
	"""
	)


def main():

	st.markdown(
		"<h1 style='text-align: center; color: Red;'>uWu Translator</h1>",
		unsafe_allow_html=True,
	)

	st.text("""""")
	st.write(
		"""
		## About
		"""
	)
	
	st.markdown("<hr>", unsafe_allow_html=True)
	st.write(
		"""
		Create your brand new uWu quote with my tools. Thanks for using.
		"""
	)

	st.markdown(
		"This project is made by <a href='https://www.iamroyakash.com'><b>theroyakash</b></a>",
		unsafe_allow_html=True,
	)

	st.text("""""")
	st.write(
		"""
		## Put your quote in the text field below and hit run.
		"""
	)

	st.markdown("<hr>", unsafe_allow_html=True)

	st.text("""""")
	inputText = st.text_input("Your Input", 'Nooo ! I was not late to work')
	st.text("""""")

	st.text("""""")
	unleashed = st.button("Unleash the uWu dog")

	if unleashed:

		try:
			input_data = str(inputText)
			y = generateUwU.generateUwU(input_data)

			show_output(y)

		except:
			st.write(
			"""
			### ❗ Oops! Server has run into some error that we are not sure about.
			"""
			)

			st.write(
			"""
			### Help me resolve this:
			- Take a screenshot of this,
			- Send me an email [here](mailto:business.theroyakash@outlook.com) 
			"""
			)

	st.text("""""")
	st.text("""""")
	st.text("""""")
	st.text("""""")
	st.text("""""")
	st.write(
	"""
	#### Made with Love by theroyakash
	"""
	)

if __name__=="__main__":
    main()
