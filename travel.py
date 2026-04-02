from random import choice
from statistics import quantiles

from pywebio.input import input, slider,select
from pywebio.output import put_markdown, put_text, put_image
from tornado.options import options
import travelcost

# Header
put_markdown("# Шкільна поїздка")
put_markdown("---")

#PRICE
put_markdown("## Ціни")
put_text(f"Bus cost={travelcost.COST_ONE_BUS} grn")
put_text(f"Train cost by one person={travelcost.COST_TRAIN_PER_ONE_PERSON} grn")
put_text(f"Hotel live per one night={travelcost.COST_LIVE_PER_ONE_NIGHT} grn")

#?????????
put_markdown("## Питання")
quantity_student = slider("How student going?", min_value=1,max_value=60,value=30, step=1)
quantity_teacher = slider("How teacher going?", min_value=1,max_value=15,value=8, step=1)
transport_choice = select("What transport you choice",['Bus','train'])
days_live = slider("How days you will live?",min_value=1,max_value=100,value=50, step=1)

#calculation

total_count_people = quantity_student + quantity_teacher
if transport_choice == 'Bus':
    bus_need = total_count_people / 40
    bus_needs = round(bus_need)


if transport_choice == 'train':
    transport_cost = total_count_people * travelcost.COST_TRAIN_PER_ONE_PERSON

if transport_choice == 'Bus':
    transport_cost = bus_needs * travelcost.COST_ONE_BUS

live_cost = total_count_people * travelcost.COST_LIVE_PER_ONE_NIGHT

total_cost = transport_cost + live_cost
discount_sume = 0
if total_count_people > travelcost.DISCOUNT_TRIGER_SUME:
    discount_sume = total_cost * travelcost.DISCOUNT_COST

total_costs = total_cost - discount_sume

put_text(f"total_count_people={total_count_people}")
put_text(f"transport_cost={transport_cost}")
put_text(f"live_cost={live_cost}")
put_text(f"Total cost={total_costs} grn")
