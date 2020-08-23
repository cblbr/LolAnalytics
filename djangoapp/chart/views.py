from django.shortcuts import render
from django import forms
from .utils import probability_prediction as pp

choices = (
    ("1", "red"),
    ("2", "blue"),
)


# def map_team(team_key):
#     if team_key == 1:
#         return "red"
#     else:
#         return "blue"


class NewTaskform(forms.Form):  # form for getting data needed for prediction
    gold_diff = forms.IntegerField(label='Gold difference')
    exp_diff = forms.IntegerField(label='Exp difference')
    team = forms.CharField(label='team')
    #todo: change team variable to be a binary choice


def index(request):
    if request.method == "POST":
        form = NewTaskform(request.POST)
        if form.is_valid():
            df = pp.predict_probability_of_winning(form.cleaned_data["gold_diff"],
                                                   form.cleaned_data["exp_diff"], form.cleaned_data["team"])
            something = round(float(df[f'{form.cleaned_data["team"]}Win']) * 100, ndigits=2)
            return render(request, 'chart/chart.html',
                          dict(probability=something))  # "something" is later inputed as gauge value
    else:
        return render(request, 'chart/getinput.html', {'form': NewTaskform()})

# inputing logic into html : {% if something %}
#                               some html
#                               {% else %}
#                               some html
#                              {% end if %}
