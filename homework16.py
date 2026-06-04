from pywebio.input import input, input_group
from pywebio.input import input, input_group
from pywebio.output import put_text, put_success
from pywebio import start_server
from pywebio.session import run_js

import homework16_utils


def get_info():
    data = input_group(
        "запит на відправку електроного листа",
        [
            input("Name", name="name", required=True),
            input("Email", name="email", required=True),
            input("string",name="string", required=True ),
        ],
    )
    recipients = [data["email"]]
    name_of_user = data["name"]
    string_of_user = data["string"]
    strip_string = string_of_user.strip()
    string_long = len(strip_string)
    data["string_long"] = string_long
    mail_body = homework16_utils.create_string_report(data)

    homework16_utils.send_email(
        recipients,
        mail_body,
        mail_subject=f"Hello {name_of_user}! You got string: {string_of_user} and they have {string_long} words ",
    )




    put_success("Email was sent. The page reloads in 5 seconds...")

    run_js("""
            setTimeout(() => {
                window.location.reload();
            }, 5000);
        """)

start_server(
    get_info,
    host="0.0.0.0",
    port=8888,
    debug=True,
)


