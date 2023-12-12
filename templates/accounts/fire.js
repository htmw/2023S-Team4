
</script>

<script type="module">
               // Import the functions you need from the SDKs you need
            import { initializeApp } from "https://www.gstatic.com/firebasejs/9.19.1/firebase-app.js";
            import { getDatabase, ref, set, get, child } from "https://www.gstatic.com/firebasejs/9.19.1/firebase-database.js";

  // Your web app's Firebase configuration
            const firebaseConfig = {
              apiKey: "AIzaSyBzyC0fZSTBoTbzsZw8eIqMduGes7_yVf4",
    authDomain: "project-62832.firebaseapp.com",
    databaseURL: "https://project-62832-default-rtdb.firebaseio.com",
    projectId: "project-62832",
    storageBucket: "project-62832.appspot.com",
    messagingSenderId: "669080652409",
    appId: "1:669080652409:web:e5c7476b70da7e59f2e2a8"
            };

  // Initialize Firebase
            const app = initializeApp(firebaseConfig);

   //get ref to database services
             const db = getDatabase(app);

             document.getElementById("submit").addEventListener('click', function(e){
              e.preventDefault();
              set(ref(db, 'user/' + document.getElementById("username").value),
              {

                username: document.getElementById("username").value,
                email: document.getElementById("email").value,
                PhoneNumber: document.getElementById("phone").value

              });
                alert("Login Sucessfull  !");
             })
        </script>