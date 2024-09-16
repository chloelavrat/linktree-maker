import streamlit as st

# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
    <link rel="icon" type="image/svg+xml" href="favicon.png">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            position: relative;
            overflow: hidden;
        }}
        .container {{
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 90%;
            max-width: 400px;
            overflow: hidden;
            position: relative;
            z-index: 100;
        }}
        .banner {{
            width: 100%;
            height: 150px;
            object-fit: cover;
        }}
        .profile-photo {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            margin-top: -75px;
            border: 5px solid white;
        }}
        h1 {{
            font-size: 24px;
            margin-bottom: 10px;
        }}
        p {{
            color: #777;
            margin-bottom: 30px;
        }}
        .link {{
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #6a0dad;
            color: white;
            text-decoration: none;
            padding: 15px;
            border-radius: 11px;
            margin: 16px 20px;
            transition: background-color 0.3s;
        }}
        .link:hover {{
            background-color: #4b0082;
        }}
        .link i {{
            margin-right: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <img src="{banner_photo}" alt="Banner Image" class="banner">
        <img src="{profile_photo}" alt="Profile Photo" class="profile-photo">
        <h1>{name}</h1>
        <p>{description}</p>
        <a href="{linkedin}" class="link"><i class="fab fa-linkedin"></i>Linkedin</a>
        <a href="{instagram}" class="link"><i class="fab fa-instagram"></i>Instagram</a>
        <a href="{twitter}" class="link"><i class="fab fa-twitter"></i>Twitter</a>
        <a href="{github}" class="link"><i class="fab fa-github"></i>GitHub</a>
        <a href="{blog}" class="link"><i class="fas fa-globe"></i>My blog</a>
    </div>
</body>
</html>
"""

# Streamlit App
st.image("./banner.png")

st.markdown("""Create professional-looking social media link cards with our easy-to-use **Linktree maker**!
            Simply fill in your profile details, add links to your social media profiles, and click the 'Generate HTML' button to download your customized link card as an HTML file. Perfect for personal branding, online presence, or promoting your work on various platforms!""")

# Using streamlit.form to organize the inputs
with st.form("profile_form"):
    name = st.text_input('Full Name', 'Ada Lovelace')
    description = st.text_input(
        'Description', 'First programmer on Earth')
    banner_photo = st.text_input(
        'Banner Photo URL', 'https://openfileserver.chloelavrat.com/stocks/web-id/banner.jpg')
    profile_photo = st.text_input(
        'Profile Photo URL', 'https://openfileserver.chloelavrat.com/stocks/web-id/ada-lovelace.jpg')
    linkedin = st.text_input('LinkedIn URL', 'https://www.linkedin.com')
    instagram = st.text_input('Instagram URL', 'https://www.instagram.com')
    twitter = st.text_input('Twitter URL', 'https://x.com')
    github = st.text_input('GitHub URL', 'https://github.com')
    blog = st.text_input('Blog URL', 'https://my-super-blog.com')

    # Submit button to submit the form
    submitted = st.form_submit_button("Generate HTML")

if submitted:
    # Create the final HTML content using the template
    html_content = html_template.format(
        name=name,
        description=description,
        banner_photo=banner_photo,
        profile_photo=profile_photo,
        linkedin=linkedin,
        instagram=instagram,
        twitter=twitter,
        github=github,
        blog=blog
    )

    # Save the HTML file
    with open("index.html", "w") as file:
        file.write(html_content)

    st.success("HTML file generated successfully!")

    # Download link
    st.download_button(
        label="Download HTML file",
        data=html_content,
        file_name="index.html",
        mime="text/html"
    )
