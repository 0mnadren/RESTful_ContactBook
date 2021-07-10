<div class="container">
    <div class="row">
        <div class="col">
            <h1 class="mt-4 mb-4">Welcome to RESTful Contact Book</h1>
            <p>My name is Nemanja, and this app is made in Django Rest Framework.</p>
            Implementations are:<ul>
                <li>CRUD is implemented for contacts</li>
                <li>When contact is deleted, its status goes to False, and it will not be shown when you list all contacts</li>
                <li>In endpoint /birthday user should provide Query parameter for filtering data</li>
                <li>I tried to implement SWAGGER, you can check it <a href="{% url 'schema-swagger-ui' %}">here</a>. For now, it is in demo state</li>
                <li>For authentication, I used <strong>JWT Token Authentication</strong></li>
            </ul>
            <h5>If you interested in my work you can check my <a href="https://nemanjadavidovic.pythonanywhere.com/">portfolio</a>
             or my <a href="https://github.com/0mnadren">GitHub page</a>.</h5>
        </div>
    </div>
    <div class="row mt-4">
        <div class="col">
            <h3>Endpoints</h3>
            <hr class="mt-4 mb-4" style="height: 3px; background:blue;">
            <ul>
                <li>
                    <h5>Check Swagger page --> <strong>(name_app)/swagger/</strong></h5>
                </li>
                <li>
                    <h5>Check Swagger Redoc --> <strong>(name_app)/redoc/</strong></h5>
                </li>
                  <li>
                    <h5>You can register at --> <strong>(name_app)/api/register/</strong></h5>
                  </li>
                  <li>
                      <h5>You can then login at --> <strong>(name_app)/api/login/</strong> <-- You will get the Access Token(last 5 minutes) and Refresher Token(last 2 days).</h5>
                  </li>
                    <li>
                      <h5>You can get new Access Token --> <strong>(name_app)/api/login/refresh/</strong> <-- If you already have a Refresher Token you can get Access Token here</h5>
                  </li>
                    <li>
                      <h5>To logout --> <strong>(name_app)/api/logout/</strong> <-- Your Refresher Token will become invalid</h5>
                  </li>
            </ul>
            <hr class="mt-4 mb-4" style="height: 3px; background:blue;">
            <ul>
              <li><h5>To see the account properties go to --> <strong>(name_app)/api/pproperties/</strong></h5></li>
              <li><h5>To edit account go to --> <strong>(name_app)/api/properties/update/</strong></h5>
            </ul>
            <hr class="mt-4 mb-4" style="height: 3px; background:blue;">
            <ul>
              <li><h5>To see the list of all 'Contacts' go to --> <strong>(name_app)/api/contacts/</strong> <-- You can also create 'Contact' there.</h5></li>
              <li><h5>To access the individual 'Contact' go to --> <strong>(name_app)/api/contacts/{int:id}</strong> <-- You can update or delete 'Contact' there.</h5></li>
              <h5>'Contact' wont be deleted instead 'active' will be set to False.</h5>
            </ul>
            <hr class="mt-4 mb-4" style="height: 3px; background:blue;">
            <ul>
              <li><h5>To filter Contacts by their birthday go to -->
                <strong>(name_app)/api/contacts/birthday/?is_older_than=YYYY-MM-DD</strong> <-- You must provide parameter.</h5></li>
              <li><h5>When you do provide parameter it will list all contacts that are older than parameter.</h5></li>
            </ul>
        </div>
    </div>
</div>
