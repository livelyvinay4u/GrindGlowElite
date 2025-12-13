import streamlit as st
from utils import apply_custom_theme
from email.message import EmailMessage
import smtplib

apply_custom_font() 

def contactus_navigation():
    # Display contact email
    st.markdown("## 📬 Contact Us")
    st.write("For any inquiries, feel free to contact us") 

# Contact form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        sender_email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            if name and sender_email and message:
                try:
                    # Email setup
                    receiver_email = "gindglowelite@gmail.com"  # Replace with your email
                    email = EmailMessage()
                    email['Subject'] = f"New Contact Form Submission from {name}"
                    email['From'] = sender_email
                    email['To'] = receiver_email
                    email.set_content(
                        f"Name: {name}\n"
                        f"Email: {sender_email}\n\n"
                        f"Message:\n{message}"
                    )

                    # SMTP server (example: Gmail)
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login("grindglowelite@gmail.com", "<16-digit-app-password>")  # Use app password
                        #smtp.login("grindglowelite@gmail.com", "")  # Use app password
                        smtp.send_message(email)

                    st.success("✅ Your message has been sent successfully!")
                except Exception as e:
                    st.error(f"❌ Failed to send message: {e}")
            else:
                st.warning("⚠️ Please fill in all fields.")