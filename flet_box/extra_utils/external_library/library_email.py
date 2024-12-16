import smtplib
from email.mime.text import MIMEText


def send_email(send_user: str = str(), send_to: str = str(), title: str = "hi there!!!", password: str = str(), personal_code: int = int(), user_name: str = str()):
    """EXEMPLE:

    send_email( send_to='kuko53348@gmail.com',
                title='JustOneClick ',
                personal_code=45545454655,
                user_name='name'
    )

    """
    user = "justoneclick37@gmail.com"
    password = "gpae milb kxlm pdoq"
    css_code = """
        <style>
            .card {
                  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                  max-width: 300px;
                  margin: auto;
                  text-align: center;
                  font-family: arial;

                }

            .title {
                  color: grey;
                  font-size: 18px;
                }

                button {
                  border: none;
                  outline: 0;
                  display: inline-block;
                  padding: 8px;
                  color: white;
                  background-color: #000;
                  text-align: center;
                  cursor: pointer;
                  width: 100%;
                  font-size: 18px;
                }

            .telegram_user {
                  text-decoration: none;
                  font-size: 32px;
                  color: Teal;
                }

            button:hover, a:hover {
                  opacity: 0.7;
                }
        """
    html = f"""\
        <!DOCTYPE html>
        <html>
            <head>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                {css_code}
                </style>
            </head>
            <body>
                <h6 style="text-align:center;opacity: 0.2;">The MIT License

            Copyright (c) 2020 WeStacks

            Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditionsThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
                </h6>
                <div class="card">
                  <img src="https://i.ibb.co/5MF1CDy/image-search-1700584447540.png" alt="John" style="width:100%">
                    <h1>{user_name}</h1>
                    <p class="title">Never share your personal password</p>
                    <p><h2><b>{personal_code}</b></h2></p>
                  <div style="margin: 24px 0;">
                    <a href="https://t.me/JustOneClic_bot"><i class="telegram_user"><b>Flet-box</b></i></a>
                  </div>
                  <p><a href="www.youtube.com/@flet-box"></a><button>@flet-box</button></a></p>
                </div>

            </body>
            <footer>
                <h6 style="text-align:center;opacity: 0.2;">The most important way to protect yourself from this type of scam is to never share a verification code of any kind with others, especially with someone you connect with through an online platform like Craigslist or Facebook. In fact, it is important that you do not share any sensitive information on these platforms, as scammers might use additional information to access your accounts or open new accounts in your name. If someone requests a verification code from you, cease communication and report the incident
                </h6>
            </footer>
        </html>
        """
    msg = MIMEText(html, 'html')
    msg['From'] = user
    msg['To'] = send_to
    msg['Subject'] = title

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(user, password)
        smtp_server.sendmail(send_user, send_to, msg.as_string())

    # print("Message sent!")
    # return "Message sent!"
    return True


if __name__ == '__main__':
    # pass
    # EXEMPLE: of use
    send_email(
                user_name='name',
                send_to='kuko53348@gmail.com',
                title='JustOneClick ',
                personal_code=45545454655,
               )
