[1mdiff --git a/lists/templates/home.html b/lists/templates/home.html[m
[1mindex 21cb0c9..08b9218 100644[m
[1m--- a/lists/templates/home.html[m
[1m+++ b/lists/templates/home.html[m
[36m@@ -1,17 +1,3 @@[m
[31m-<html>[m
[31m-  <head>[m
[31m-    <title>To-Do lists</title>[m
[31m-  </head>[m
[31m-  <body>[m
[31m-    <h1>Your To-Do list</h1>[m
[31m-    <form method="POST" action="/lists/new">[m
[31m-      <input name="item_text" id="id_new_item"  placeholder="Enter a to-do item"/>[m
[31m-      {% csrf_token %}[m
[31m-    </form>[m
[31m-    <table id="id_list_table">[m
[31m-      {% for item in items %}[m
[31m-        <tr><td>{{ forloop.counter }}: {{ item.text }}</td></tr>[m
[31m-      {% endfor %}[m
[31m-    </table>[m
[31m-  </body>[m
[31m-</html>[m
[32m+[m[32m{% extends 'base.html' %}[m
[32m+[m[32m{% block header_text %}Start a new To-Do list{% endblock %}[m
[32m+[m[32m{% block form_action %}/lists/new{% endblock %}[m
[1mdiff --git a/lists/templates/list.html b/lists/templates/list.html[m
[1mindex 9fe6228..4fc4d44 100644[m
[1m--- a/lists/templates/list.html[m
[1m+++ b/lists/templates/list.html[m
[36m@@ -1,17 +1,10 @@[m
[31m-<html>[m
[31m-  <head>[m
[31m-    <title>To-Do lists</title>[m
[31m-  </head>[m
[31m-  <body>[m
[31m-    <h1>Your To-Do list</h1>[m
[31m-    <form method="POST" action="/lists/new">[m
[31m-      <input name="item_text" id="id_new_item" placeholder="Enter a to-do item"/>[m
[31m-      {% csrf_token %}[m
[31m-    </form>[m
[32m+[m[32m{% extends 'base.html' %}[m
[32m+[m[32m{% block header_text %}Your To-Do list{% endblock %}[m
[32m+[m[32m{% block form_action %}/lists/{{ list.id }}/add_item{% endblock %}[m
[32m+[m[32m{% block table %}[m
   <table id="id_list_table">[m
[31m-      {% for item in items %}[m
[32m+[m[32m    {% for item in list.item_set.all %}[m
     <tr><td>{{ forloop.counter }}: {{ item.text }}</td></tr>[m
     {% endfor %}[m
   </table>[m
[31m-  </body>[m
[31m-</html>[m
[32m+[m[32m{% endblock %}[m
