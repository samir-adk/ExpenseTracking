from django.test import TestCase

# <form method="POST" enctype="multipart/form-data" action="{% url 'authentication:register' %}">
# {% csrf_token %}
# {{form}}
# <input type="submit" name="submit">
# </form>