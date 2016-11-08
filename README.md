This is guidelines - an [OPAL](https://github.com/openhealthcare/opal) plugin.

# Installation

Install this module

Add 'guidelines' to installed apps.

Run

   $ python manage.py migrate

Add the guideline template tag wherever you want to display guidelines e.g.

    <!-- ./yourapp/templates/records/diagnosis.html -->
    {% load guideline %}
    [[item.date_of_diagnosis | shortDate]]
    <span ng-show="item.provisional">?</span>
      [[item.condition]]
    <span ng-show="item.details">([[item.details]])</span>
    {% guideline_for "item.condition" %}
