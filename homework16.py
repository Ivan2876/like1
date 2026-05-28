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
            input("Email", name="email", required=True)
        ]
    )

# name_of_user = homework16_utils.get_user_info(data["name"])





